"""Check exact package allowlists, indexed fidelity and standalone installation."""
from pathlib import Path,PurePosixPath
from contextlib import closing
import hashlib,json,os,sqlite3,subprocess,sys,tempfile,zipfile
ROOT=Path(__file__).resolve().parents[1]
def digest(path):
 with path.open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()
def run(script,*args,cwd=None,success=True):
 env=dict(os.environ);env.pop('VAELTHARYN_ROOT',None)
 r=subprocess.run([sys.executable,'-X','utf8',str(script),*map(str,args)],cwd=cwd,env=env,capture_output=True,text=True,encoding='utf-8')
 assert (r.returncode==0)==success,(r.returncode,r.stderr);return r.stdout
def skill_files(m):
 paths={'SKILL.md','agents/openai.yaml','scripts/chercher.py','references/edition.json','references/translation-cautions.md','references/corpus/corpus.json','references/corpus/LICENSE.md','references/corpus/data/search.sqlite3'}
 paths|={'scripts/vaeltharyn/'+p.name for p in (ROOT/'vaeltharyn').glob('*.py')}
 paths|={'references/corpus/'+name for name in m['packaged_documents']}
 paths|={'references/corpus/data/provenance/'+name for name in ('integrity.json','NOTICE.md','references.json')}
 return paths
def check_skill(skill,cwd):
 corpus=skill/'references/corpus';m=json.loads((corpus/'corpus.json').read_text(encoding='utf-8'))
 assert m['corpus_version']=='1.6.0' and m['structure_version']=='4.1.0' and m['distribution']['format']=='indexed'
 path=corpus/m['distribution']['index'];assert digest(path)==m['distribution']['index_sha256']
 with closing(sqlite3.connect(path.as_uri()+'?mode=ro',uri=True)) as db:
  assert db.execute('PRAGMA quick_check').fetchone()[0]=='ok'
  assert db.execute("SELECT count(*) FROM records WHERE kind='entry'").fetchone()[0]==65045
  assert db.execute("SELECT count(*) FROM records WHERE kind='expression'").fetchone()[0]==456
  allowed={'id','key','vaeltharyn','francais','english','francais_controle','english_checked','litteral_fr','literal_en','intensite','fonction','statut','type_equivalence','force','note_fr','note_en','references','expression_id','lexique_ids','analyses_lexicales','traitement','schema_a_completer','slots','corpus_registry','source_file','aliases'}
  for raw, in db.execute("SELECT payload FROM records WHERE kind='expression'"):
   item=json.loads(raw);assert not set(item)-allowed
   for alias in item['aliases']:assert set(alias)=={'lang','term','note_fr','note_en'}
 script=skill/'scripts/chercher.py';r=json.loads(run(script,'--lang','en','harmonic frequency','exchange for mine',cwd=cwd))
 assert Path(r['corpus_root']).resolve()==corpus.resolve()
 assert r['results']['harmonic frequency']['expressions'][0]['vaeltharyn']=='korthir goesumen'
 assert r['results']['exchange for mine']['expressions'][0]['schema_a_completer']
 r2=json.loads(run(script,'--lang','fr','faim',cwd=cwd));assert r2['results']['faim']['entries'][0]['word']=='haem'
 cases=json.loads(run(script,'--lang','vh','Thalen moelom!',cwd=cwd));assert {'weird_warning','unusual'}<={v.get('key') for v in cases['results']['Thalen moelom!']['expressions']}
 added=json.loads(run(script,'--lang','fr','désir','cœur','silence','tu me manques',cwd=cwd))
 for term,word in [('désir','vael'),('cœur','naevan'),('silence','thaemnyr')]:
  assert any(e['word']==word and e.get('alias_matches') for e in added['results'][term]['entries'])
 assert any(e.get('key')=='absence_felt' for e in added['results']['tu me manques']['expressions'])
 forms=json.loads(run(script,'--lang','en','hesitate','sigh of relief',cwd=cwd))
 assert any(e['word']=='trukoemar' for e in forms['results']['hesitate']['entries'])
 assert any(e['word']=='saelraev-dathak' for e in forms['results']['sigh of relief']['entries'])
 run(script,'--root',cwd/'absent','--lang','fr','faim',cwd=cwd,success=False)
 run(script,'--lang','fr','faim','--limit','101',cwd=cwd,success=False)
 return r['results']
def main():
 release=json.loads((ROOT/'integrations/release.json').read_text(encoding='utf-8'));m=json.loads((ROOT/'corpus.json').read_text(encoding='utf-8'));layout=skill_files(m)
 (ROOT/'dist').mkdir(exist_ok=True)
 with tempfile.TemporaryDirectory(prefix='check-',dir=ROOT/'dist') as tmp:
  temp=Path(tmp);assert temp.resolve().is_relative_to((ROOT/'dist').resolve())
  for kind in ('plugin','skill'):
   path=ROOT/'dist/releases'/release[kind]['file'];assert digest(path)==release[kind]['sha256']
   expected=layout if kind=='skill' else {'plugin.json','.codex-plugin/plugin.json','README.md'}|{'skills/translate-vaeltharyn/'+p for p in layout}
   with zipfile.ZipFile(path) as archive:
    assert set(archive.namelist())==expected,(kind,set(archive.namelist())-expected,expected-set(archive.namelist()))
    assert archive.testzip() is None
    for name in archive.namelist():
     p=PurePosixPath(name);assert not p.is_absolute() and '..' not in p.parts and ':' not in name and '\\' not in name
    archive.extractall(temp/kind)
  a=json.loads((temp/'plugin/plugin.json').read_text(encoding='utf-8'));b=json.loads((temp/'plugin/.codex-plugin/plugin.json').read_text(encoding='utf-8'))
  assert a['name']==b['name']=='vaeltharyn-translator' and a['version']==b['version']=='0.8.0'
  assert a['author']['name']==b['author']['name']=='SheIsZoe'
  assert a['extensions']['com.openai']['interface']==b['interface']
  assert check_skill(temp/'skill',temp)==check_skill(temp/'plugin/skills/translate-vaeltharyn',temp)
  destination=temp/'catalogue avec espaces'
  for _ in range(2):run(ROOT/'scripts/installer_plugin.py','--destination',destination,cwd=temp)
  (destination/'plugins/vaeltharyn-translator/README.md').write_text('local edit',encoding='utf-8')
  run(ROOT/'scripts/installer_plugin.py','--destination',destination,cwd=temp,success=False)
 report={'status':'pass','plugin_version':'0.8.0','corpus_version':'1.6.0','structure_version':'4.1.0','exact_package_allowlists':True,'indexed_expression_schema':True,'standalone_lookup':True,'installation_protection':True}
 (ROOT/'docs/quality').mkdir(exist_ok=True);(ROOT/'docs/quality/packages.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
