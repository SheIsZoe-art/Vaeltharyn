"""Vérifie le paquet autonome et la préparation d’une installation dans un dossier temporaire."""
from pathlib import Path
import hashlib,json,re,subprocess,sys,tempfile,zipfile

ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/'distributions/vaeltharyn-translator-0.4.0.zip'
def run(*args):return subprocess.check_output([sys.executable,'-X','utf8',*map(str,args)],encoding='utf-8')

(ROOT/'dist').mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(prefix='verification-',dir=ROOT/'dist') as temp:
 assert Path(temp).resolve().is_relative_to((ROOT/'dist').resolve())
 destination=Path(temp)/'catalogue avec espaces'
 for _ in range(2):run(ROOT/'scripts/installer_plugin.py','--destination',destination)
 catalog=json.loads((destination/'.agents/plugins/marketplace.json').read_text(encoding='utf-8'))
 plugin=destination/catalog['plugins'][0]['source']['path']
 assert plugin.resolve().is_relative_to(destination.resolve())
 with zipfile.ZipFile(ARCHIVE) as archive:
  assert archive.testzip() is None
  for name in archive.namelist():
   assert archive.read(name)==(plugin/name).read_bytes(),name
  source=ROOT/'plugins/vaeltharyn-translator'
  for name in ['plugin.json','skills/translate-vaeltharyn/SKILL.md','skills/translate-vaeltharyn/scripts/chercher.py','skills/translate-vaeltharyn/agents/openai.yaml','skills/translate-vaeltharyn/references/edition.json']:
   assert archive.read(name).replace(b'\r\n',b'\n')==(source/name).read_bytes().replace(b'\r\n',b'\n'),name
 manifest=json.loads((plugin/'plugin.json').read_text(encoding='utf-8'))
 assert manifest['version']=='0.4.0' and manifest['name']=='vaeltharyn-translator'
 assert manifest['author']['name']=='SheIsZoe'
 assert manifest['extensions']['com.openai']['interface']['developerName']=='SheIsZoe'
 skill=plugin/'skills/translate-vaeltharyn'
 edition=json.loads((skill/'references/edition.json').read_text(encoding='utf-8'))
 for name,digest in edition['sha256'].items():
  assert hashlib.sha256((skill/'references/corpus'/name).read_bytes()).hexdigest()==digest,name
 def query(lang,term):
  return json.loads(run(skill/'scripts/chercher.py','--root',skill/'references/corpus','--lang',lang,term,'--limit','2'))['results'][term]
 assert query('vh','slusoemar')['entries'][0]['valence']=='tr'
 assert query('en','badass')['expressions'][0]['key']=='badass'
 assert query('fr','Gognand')['expressions'][0]['vaeltharyn']==''
 assert query('en','harmonic frequency')['expressions'][0]['vaeltharyn']=='korthir goesumen'
 assert query('vh','saevron')['entries'][0]['definition_fr'].startswith('Partie du tronc')
 assert query('en','exchange for mine')['expressions'][0]['schema_a_completer']
 assert edition['entries']==65041
 # Refuse a different file instead of overwriting a prior installation.
 (plugin/'plugin.json').write_text('{}',encoding='utf-8')
 failed=subprocess.run([sys.executable,str(ROOT/'scripts/installer_plugin.py'),'--destination',str(destination)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 assert failed.returncode==2 and (plugin/'plugin.json').read_text(encoding='utf-8')=='{}'

for doc in [ROOT/'INSTALLATION.md',ROOT/'plugins/vaeltharyn-translator/README.md']:
 for target in re.findall(r'\]\(([^)]+)\)',doc.read_text(encoding='utf-8')):
  if target.startswith('https://'):continue
  assert (doc.parent/target.split('#')[0]).is_file(),target
report={'status':'pass','plugin_version':'0.4.0','corpus_edition':'1.5.0','corpus_revision':edition['revision'],'archive_sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),'checks':['archive integrity','identical bundled source','installation in path with spaces','idempotent preparation','refusal to overwrite different files','embedded corpus hashes','FR/EN/Vaeltharyn queries','uncertain expression preserved','documentation local links'],'scope':'package preparation and lookup verified; host installation commands follow official Codex documentation'}
(ROOT/'distributions/verification-0.4.0.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
