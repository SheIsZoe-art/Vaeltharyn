"""Indexed lookup; source CSV and JSON remain authoritative."""
import argparse, csv, hashlib, json, os, sqlite3, sys, tempfile, unicodedata
from pathlib import Path
from contextlib import closing
from .resources import root_path, manifest

SCHEMA = 1
def norm(s):
    return ' '.join(unicodedata.normalize('NFC', str(s)).casefold().replace('’', "'").strip(' \t\r\n!?.,;').split())

def rows(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        yield from csv.DictReader(f, delimiter=';')

def sources(root, m):
    paths = [x['detailed'] for x in m['lexicon'].values()]
    for registry in m['expressions']:
        paths.extend(registry[k] for k in ('records', 'routes', 'aliases') if k in registry)
    return paths

def fingerprint(root, m):
    state = [(p, (root/p).stat().st_size, (root/p).stat().st_mtime_ns) for p in sources(root,m)]
    return hashlib.sha256(json.dumps([m,state],sort_keys=True).encode()).hexdigest()

def expressions(root, m):
    for registry in m['expressions']:
        records = json.loads((root/registry['records']).read_text(encoding='utf-8'))
        routes = json.loads((root/registry['routes']).read_text(encoding='utf-8')) if 'routes' in registry else []
        aliases = list(rows(root/registry['aliases'])) if 'aliases' in registry else []
        for raw in records:
            key = raw.get('key',raw.get('id'))
            payload = dict(raw, corpus_registry=registry['id'], source_file=registry['records'])
            attached = [r for r in routes if key in r['sens_cles']]
            payload['source_routes'] = attached
            attached_aliases = [r for r in aliases if r['id_expression']==key]
            payload['lookup_aliases'] = attached_aliases
            terms = {'vh':[raw['vaeltharyn']], 'fr':[raw.get('francais_controle',raw.get('francais',''))], 'en':[raw.get('english_checked',raw.get('english',''))]}
            for lang in ('fr','en'):
                terms[lang] += raw.get('aliases_'+lang,[]) + [r['source'] for r in attached if r['langue']==lang] + [r['recherche'] for r in attached_aliases if r['lang']==lang]
            if raw.get('source_en'): terms['en'].append(raw['source_en'])
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
        db.executescript('PRAGMA journal_mode=OFF; PRAGMA synchronous=OFF; CREATE TABLE meta(key TEXT PRIMARY KEY,value TEXT); CREATE TABLE records(kind TEXT,key TEXT,payload TEXT,PRIMARY KEY(kind,key)); CREATE TABLE terms(lang TEXT,term TEXT,kind TEXT,key TEXT); CREATE TABLE texts(lang TEXT,kind TEXT,key TEXT,value TEXT);')
        def insert(kind,key,payload,terms,notes):
            db.execute('INSERT INTO records VALUES(?,?,?)',(kind,key,json.dumps(payload,ensure_ascii=False,separators=(',',':'))))
            for lang,values in terms.items():
                unique=set(norm(v) for v in values if v)
                db.executemany('INSERT INTO terms VALUES(?,?,?,?)',[(lang,v,kind,key) for v in unique])
                # Contains lookup is intentionally a slower scan, including notes/definitions.
                db.execute('INSERT INTO texts VALUES(?,?,?,?)',(lang,kind,key,'\n'.join(sorted(unique | {norm(notes.get(lang,''))}))))
        fr=list(rows(root/m['lexicon']['fr']['detailed'])); en=list(rows(root/m['lexicon']['en']['detailed']))
        if len(fr)!=len(en) or len(fr)!=m['counts']['entries']:raise ValueError('Lexicon count mismatch')
        for f,e in zip(fr,en):
            if f['id']!=e['id']:raise ValueError('Bilingual ID mismatch')
            insert('entry',f['id'],{'fr':f,'en':e},{'vh':[f['mot']],'fr':[f['francais'],f['sens']],'en':[e['english_headword'],e['meaning']]},{'fr':f.get('definition_fr',''),'en':e.get('definition_en',''),'vh':f.get('definition_fr','')})
        count=0
        for key,payload,terms in expressions(root,m):
            insert('expression',key,payload,terms,{'fr':payload.get('note_fr',''),'en':payload.get('note_en','')});count+=1
        db.executescript('CREATE INDEX exact_lookup ON terms(lang,term); CREATE INDEX text_language ON texts(lang);')
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
                hits=db.execute('SELECT DISTINCT kind,key FROM texts WHERE lang=? AND instr(value,?)>0 ORDER BY kind,key',(lang,value)).fetchall()
            elif mode=='prefix':
                hits=db.execute('SELECT DISTINCT kind,key FROM terms WHERE lang=? AND term>=? AND term<? ORDER BY kind,key',(lang,value,value+'\U0010ffff')).fetchall()
            else:
                hits=db.execute('SELECT DISTINCT kind,key FROM terms WHERE lang=? AND term=? ORDER BY kind,key',(lang,value)).fetchall()
            result={'total':0,'entries':[],'expression_total':0,'expressions':[]}
            seen_expressions=set()
            for kind,key in hits:
                target='entries' if kind=='entry' else 'expressions';counter='total' if kind=='entry' else 'expression_total'
                raw=None
                if kind=='expression':
                    raw=json.loads(db.execute('SELECT payload FROM records WHERE kind=? AND key=?',(kind,key)).fetchone()[0])
                    identity=raw.get('expression_id') or raw.get('id') or key
                    # Suppress the old registry copy only; distinct contextual
                    # senses can legitimately share one canonical expression.
                    if raw['corpus_registry']=='register-1.3.0' and identity in seen_expressions:continue
                    seen_expressions.add(identity)
                result[counter]+=1
                if len(result[target])>=limit:continue
                if raw is None:raw=json.loads(db.execute('SELECT payload FROM records WHERE kind=? AND key=?',(kind,key)).fetchone()[0])
                if kind=='entry':payload=(raw['en' if lang=='en' else 'fr'] if full else compact_entry(raw))
                else:
                    payload=raw if full else {k:v for k,v in raw.items() if k not in ('source_routes','lookup_aliases','analyses_lexicales')}
                    payload=dict(payload,source_matches=[r for r in raw['source_routes'] if r['langue']==lang and (value in norm(r['source']) if mode=='contains' else norm(r['source']).startswith(value) if mode=='prefix' else norm(r['source'])==value)])
                    payload['alias_matches']=[r for r in raw['lookup_aliases'] if r['lang']==lang and (value in norm(r['recherche']) if mode=='contains' else norm(r['recherche']).startswith(value) if mode=='prefix' else norm(r['recherche'])==value)]
                result[target].append(payload)
            results[term]=result
    finally:db.close()
    return {'corpus_root':str(root),'edition':m['corpus_version'],'structure_version':m['structure_version'],'mode':mode,'results':results}

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
