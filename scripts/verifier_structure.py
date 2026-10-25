"""Check lossless relocation, indexed fidelity, contextual regressions and links."""
from pathlib import Path
from contextlib import closing
import csv,hashlib,json,posixpath,re,sqlite3,subprocess,sys,urllib.parse
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from vaeltharyn.resources import manifest
from vaeltharyn.search import connect,lookup,rows

def check_links():
    existing={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and not any(s in p.parts for s in ('.git','dist','.cache'))}
    broken=set();checked=0
    for name in existing:
        if not name.endswith('.md'):continue
        text=(ROOT/name).read_text(encoding='utf-8-sig')
        for link in re.findall(r'\]\(([^)\n]+)\)',text):
            parsed=urllib.parse.urlsplit(link.strip('<>'))
            if parsed.scheme or parsed.netloc or not parsed.path:continue
            target=posixpath.normpath(posixpath.join(posixpath.dirname(name),urllib.parse.unquote(parsed.path)))
            checked+=1
            if target not in existing and not (ROOT/target).is_dir():broken.add((name,link,target))
    return checked,sorted(broken)

def main():
    m=manifest(ROOT);mapping=json.loads((ROOT/'archives/legacy-paths.json').read_text(encoding='utf-8'))['files']
    count=0
    for old,new in mapping.items():
        if not new.startswith('data/'):continue
        before=subprocess.check_output(['git','show','90cbfb4:'+old],cwd=ROOT)
        after=(ROOT/new).read_bytes()
        # Git normalizes text at checkout; explicitly protected provenance is binary.
        protected=new.endswith(('inventaire-fourni.txt','source_utilisateur.txt'))
        assert (before==after if protected else before.replace(b'\r\n',b'\n')==after.replace(b'\r\n',b'\n')),new
        count+=1
    with closing(connect(ROOT,m)) as db:
        stored={key:json.loads(raw) for key,raw in db.execute("SELECT key,payload FROM records WHERE kind='entry'")}
        assert len(stored)==65041
        for lang in ('fr','en'):
            for row in rows(ROOT/m['lexicon'][lang]['detailed']):assert stored[row['id']][lang]==row,row['id']
        assert db.execute("SELECT count(*) FROM records WHERE kind='expression'").fetchone()[0]==416
        assert db.execute('PRAGMA quick_check').fetchone()[0]=='ok'
    def expressions(term,lang='en'):
        result=lookup(ROOT,lang,[term],100)['results'][term]
        return result['expressions']
    assert any(s['vaeltharyn']=='korthir goesumen' for s in expressions('harmonic frequency'))
    assert any(s.get('schema_a_completer') for s in expressions('exchange for mine'))
    assert any(not s['vaeltharyn'] for s in expressions('Gognand','fr'))
    assert any(s['vaeltharyn'] for s in expressions('badass'))
    assert {'weird_warning','unusual'}<={s.get('key') for s in expressions('Thalen moelom!','vh')}
    assert lookup(ROOT,'en',['synthesizer'])['results']['synthesizer']['total']>0
    assert lookup(ROOT,'fr',['faim'])['results']['faim']['entries'][0]['word']=='haem'
    assert lookup(ROOT,'vh',['saevron'])['results']['saevron']['total']==1
    assert lookup(ROOT,'en',['synth'],mode='prefix')['results']['synth']['total']>0
    assert lookup(ROOT,'en',['waiting height'],mode='contains')['results']['waiting height']['expression_total']>0
    checked,broken=check_links()
    report={'status':'pass' if not broken else 'links_require_review','preserved_source_files':count,'indexed_entries_verified_field_by_field':65041,'context_records':416,'local_markdown_links_checked':checked,'broken_links':broken}
    (ROOT/'.cache').mkdir(exist_ok=True)
    (ROOT/'.cache/structure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='broken_links'}|{'broken_link_count':len(broken)},indent=2))
    if broken:sys.exit(1)

if __name__=='__main__':main()
