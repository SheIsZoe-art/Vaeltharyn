"""Indexed lookup; source CSV and JSON remain authoritative."""
import argparse, csv, hashlib, json, os, sqlite3, sys, tempfile, unicodedata
from pathlib import Path
from contextlib import closing
from .resources import root_path, manifest

SCHEMA = 2
def norm(s):
    return ' '.join(unicodedata.normalize('NFC', str(s)).casefold().replace('’', "'").strip(' \t\r\n!?.,;').split())

def rows(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        yield from csv.DictReader(f, delimiter=';')

def sources(root, m):
    paths = [x['detailed'] for x in m['lexicon'].values()]
    for registry in m['expressions']:
        paths.append(registry['records'])
    paths.extend([m['aliases'],m['references']])
    return paths

def fingerprint(root, m):
    state = [(p, (root/p).stat().st_size, (root/p).stat().st_mtime_ns) for p in sources(root,m)]
    return hashlib.sha256(json.dumps([m,state],sort_keys=True).encode()).hexdigest()

def expressions(root, m):
    aliases=json.loads((root/m['aliases']).read_text(encoding='utf-8'))
    by_record={}
    for alias in aliases:
        for target in alias['targets']:
            by_record.setdefault((target['registry'],target['key']),[]).append({k:v for k,v in alias.items() if k!='targets'})
    for registry in m['expressions']:
        records = json.loads((root/registry['records']).read_text(encoding='utf-8'))
        for raw in records:
            key = raw.get('key',raw.get('id'))
            payload = dict(raw, corpus_registry=registry['id'], source_file=registry['records'])
            attached=by_record.get((registry['id'],key),[])
            payload['aliases']=attached
            terms = {'vh':[raw['vaeltharyn']], 'fr':[raw.get('francais_controle',raw.get('francais',''))], 'en':[raw.get('english_checked',raw.get('english',''))]}
            for lang in ('fr','en'):
                terms[lang] += [r['term'] for r in attached if r['lang']==lang]
            yield registry['id']+':'+key,payload,terms

def build(root, destination=None):
    m=manifest(root)
    if m['distribution']['format']!='source': raise ValueError('Cannot rebuild an indexed snapshot; use the source repository.')
    destination=destination or root/'.cache/search.sqlite3'
    destination.parent.mkdir(parents=True,exist_ok=True)
    stamp=fingerprint(root,m)
    fd,tmp=tempfile.mkstemp(prefix='search-',suffix='.sqlite3',dir=destination.parent);os.close(fd)
    try:
        db=sqlite3.connect(tmp)
        db.execute('PRAGMA page_size=4096')
        db.executescript('PRAGMA journal_mode=OFF; PRAGMA synchronous=OFF; CREATE TABLE meta(key TEXT PRIMARY KEY,value TEXT); CREATE TABLE records(id INTEGER PRIMARY KEY,kind TEXT,key TEXT,payload TEXT,UNIQUE(kind,key)); CREATE TABLE terms(lang TEXT,term TEXT,record_id INTEGER); CREATE TABLE extra_values(id INTEGER PRIMARY KEY,value TEXT); CREATE TABLE extra_links(lang TEXT,record_id INTEGER,value_id INTEGER,PRIMARY KEY(lang,record_id,value_id));')
        extra_ids={}
        def insert(kind,key,payload,terms,notes):
            record_id=db.execute('INSERT INTO records(kind,key,payload) VALUES(?,?,?)',(kind,key,json.dumps(payload,ensure_ascii=False,separators=(',',':')))).lastrowid
            for lang,values in terms.items():
                unique=set(norm(v) for v in values if v)
                db.executemany('INSERT INTO terms VALUES(?,?,?)',[(lang,v,record_id) for v in unique])
                additional=notes.get(lang,[])
                if isinstance(additional,str):additional=[additional]
                # Index only text absent from the term fields; shared notes are interned.
                for extra in {norm(v) for v in additional if v}:
                    if any(extra in term for term in unique):continue
                    if extra not in extra_ids:extra_ids[extra]=db.execute('INSERT INTO extra_values(value) VALUES(?)',(extra,)).lastrowid
                    db.execute('INSERT OR IGNORE INTO extra_links VALUES(?,?,?)',(lang,record_id,extra_ids[extra]))
        fr=list(rows(root/m['lexicon']['fr']['detailed'])); en=list(rows(root/m['lexicon']['en']['detailed']))
        if len(fr)!=len(en) or len(fr)!=m['counts']['entries']:raise ValueError('Lexicon count mismatch')
        lexical_aliases={}
        for alias in json.loads((root/m['aliases']).read_text(encoding='utf-8')):
            for target in alias['targets']:
                if target['registry']=='lexicon':
                    lexical_aliases.setdefault(target['key'],[]).append({k:v for k,v in alias.items() if k!='targets'})
        for f,e in zip(fr,en):
            if f['id']!=e['id']:raise ValueError('Bilingual ID mismatch')
            attached=lexical_aliases.get(f['id'],[])
            terms={'vh':[f['mot']],'fr':[f['francais'],f['sens']],'en':[e['english_headword'],e['meaning']]}
            for lang in ('fr','en'):terms[lang]+=[a['term'] for a in attached if a['lang']==lang]
            payload={'fr':f,'en':e}
            if attached:payload['aliases']=attached
            insert('entry',f['id'],payload,terms,{'fr':[f.get('definition_fr',''),f.get('note','')],'en':[e.get('definition_en',''),e.get('note','')]})
        count=0
        for key,payload,terms in expressions(root,m):
            insert('expression',key,payload,terms,{'fr':payload.get('note_fr',''),'en':payload.get('note_en','')});count+=1
        db.executescript('CREATE INDEX exact_lookup ON terms(lang,term); CREATE INDEX extra_language ON extra_links(lang,value_id);')
        meta={'schema_version':SCHEMA,'fingerprint':stamp,'corpus_version':m['corpus_version'],'entries':len(fr),'expressions':count,'source_sha256':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in sources(root,m)}}
        db.executemany('INSERT INTO meta VALUES(?,?)',[(k,json.dumps(v,ensure_ascii=False)) for k,v in meta.items()]);db.commit()
        assert db.execute('PRAGMA quick_check').fetchone()[0]=='ok'
        db.close();os.replace(tmp,destination)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)
    return destination

def connect(root,m):
    indexed=m['distribution']['format']=='indexed'
    path=root/m['distribution']['index'] if indexed else root/'.cache/search.sqlite3'
    if not indexed:
        fresh=False
        if path.is_file():
            try:
                with closing(sqlite3.connect(path.as_uri()+'?mode=ro',uri=True)) as db:
                    fresh=json.loads(db.execute("SELECT value FROM meta WHERE key='fingerprint'").fetchone()[0])==fingerprint(root,m)
            except (sqlite3.Error,TypeError,ValueError):pass
        if not fresh:build(root,path)
    db=sqlite3.connect(path.resolve().as_uri()+'?mode=ro',uri=True)
    if json.loads(db.execute("SELECT value FROM meta WHERE key='schema_version'").fetchone()[0])!=SCHEMA:raise ValueError('Unsupported index schema')
    if json.loads(db.execute("SELECT value FROM meta WHERE key='corpus_version'").fetchone()[0])!=m['corpus_version']:raise ValueError('Index/corpus version mismatch')
    return db

def compact_entry(raw):
    f,e=raw['fr'],raw['en']
    names={'id':'id','mot':'word','categorie':'category','valence':'valency','api':'ipa','registre':'register','statut':'status','source':'source','source_licence':'source_license'}
    out={target:f.get(source,'') for source,target in names.items()}
    out.update(francais=f['francais'],english=e['english_headword'],definition_fr=f.get('definition_fr',''),definition_en=e.get('definition_en',''),note_fr=f.get('note',''),note_en=e.get('note',''))
    out['source_license']=e.get('source_license') or out['source_license']
    out['review']=e.get('review','');out['valency_en']=e.get('valency_en','')
    return {k:v for k,v in out.items() if v!=''}

def lookup(root,lang,terms,limit=8,mode='exact',full=False):
    m=manifest(root);db=connect(root,m);results={}
    try:
        for term in terms:
            value=norm(term)
            if not value:raise ValueError('Empty search term')
            if mode=='contains':
                hits=db.execute('SELECT r.kind AS kind,r.key AS key FROM terms t JOIN records r ON r.id=t.record_id WHERE t.lang=? AND instr(t.term,?)>0 UNION SELECT r.kind AS kind,r.key AS key FROM extra_links x JOIN extra_values e ON e.id=x.value_id JOIN records r ON r.id=x.record_id WHERE x.lang=? AND instr(e.value,?)>0 ORDER BY kind,key',(lang,value,lang,value)).fetchall()
            elif mode=='prefix':
                hits=db.execute('SELECT DISTINCT r.kind,r.key FROM terms t JOIN records r ON r.id=t.record_id WHERE t.lang=? AND t.term>=? AND t.term<? ORDER BY r.kind,r.key',(lang,value,value+'\U0010ffff')).fetchall()
            else:
                hits=db.execute('SELECT DISTINCT r.kind,r.key FROM terms t JOIN records r ON r.id=t.record_id WHERE t.lang=? AND t.term=? ORDER BY r.kind,r.key',(lang,value)).fetchall()
            result={'total':0,'entries':[],'expression_total':0,'expressions':[]}
            seen_expressions=set()
            for kind,key in hits:
                target='entries' if kind=='entry' else 'expressions';counter='total' if kind=='entry' else 'expression_total'
                raw=None
                if kind=='expression':
                    raw=json.loads(db.execute('SELECT payload FROM records WHERE kind=? AND key=?',(kind,key)).fetchone()[0])
                    identity=raw.get('expression_id') or raw.get('id') or key
                    # Deduplicate register wording; contextual senses remain distinct.
                    if raw['corpus_registry']=='register' and identity in seen_expressions:continue
                    seen_expressions.add(identity)
                result[counter]+=1
                if len(result[target])>=limit:continue
                if raw is None:raw=json.loads(db.execute('SELECT payload FROM records WHERE kind=? AND key=?',(kind,key)).fetchone()[0])
                if kind=='entry':
                    payload=(raw['en' if lang=='en' else 'fr'] if full else compact_entry(raw))
                    matches=[r for r in raw.get('aliases',[]) if r['lang']==lang and (value in norm(r['term']) if mode=='contains' else norm(r['term']).startswith(value) if mode=='prefix' else norm(r['term'])==value)]
                    if matches:payload=dict(payload,alias_matches=matches)
                else:
                    payload=raw if full else {k:v for k,v in raw.items() if k not in ('aliases','analyses_lexicales')}
                    payload=dict(payload,alias_matches=[r for r in raw['aliases'] if r['lang']==lang and (value in norm(r['term']) if mode=='contains' else norm(r['term']).startswith(value) if mode=='prefix' else norm(r['term'])==value)])
                result[target].append(payload)
            results[term]=result
    finally:db.close()
    catalog=json.loads((root/m['references']).read_text(encoding='utf-8'))
    selected=set()
    for result in results.values():
        for entry in result['entries']:
            for field in ('source_licence','source_license'):
                if entry.get(field):selected.add(entry[field])
        for expression in result['expressions']:selected.update(expression.get('references',[]))
    return {'corpus_root':str(root),'edition':m['corpus_version'],'structure_version':m['structure_version'],'mode':mode,'results':results,'references':{r['id']:r for r in catalog if r['id'] in selected}}

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('terms',nargs='*');parser.add_argument('--lang',choices=['fr','en','vh'])
    parser.add_argument('--root',type=Path);parser.add_argument('--limit',type=int,default=8);parser.add_argument('--full',action='store_true')
    group=parser.add_mutually_exclusive_group();group.add_argument('--contains',action='store_true');group.add_argument('--prefix',action='store_true')
    parser.add_argument('--info',action='store_true');parser.add_argument('--build-index',action='store_true')
    a=parser.parse_args(argv)
    if not 1<=a.limit<=100:parser.error('--limit must be between 1 and 100')
    try:
        root=root_path(a.root)
        if a.build_index:out={'index':str(build(root))}
        elif a.info:out=manifest(root)
        else:
            if not a.terms or not a.lang:parser.error('Provide --lang and at least one term')
            out=lookup(root,a.lang,a.terms,a.limit,'contains' if a.contains else 'prefix' if a.prefix else 'exact',a.full)
        print(json.dumps(out,ensure_ascii=False,indent=2))
    except (OSError,ValueError,KeyError,sqlite3.Error,csv.Error) as error:parser.exit(2,f'Corpus error: {error}\n')

if __name__=='__main__':main()
