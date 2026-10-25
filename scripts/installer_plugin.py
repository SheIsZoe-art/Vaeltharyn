"""Prépare le plugin autonome et son catalogue local, sans modifier Codex."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,stat,zipfile

ROOT=Path(__file__).resolve().parents[1]
LATEST=json.loads((ROOT/'distributions/latest.json').read_text(encoding='utf-8'))
VERSION=LATEST['plugin_version']
ARCHIVE=ROOT/'distributions'/LATEST['plugin']['file']

def prepare(destination):
 expected=(ARCHIVE.with_suffix('.zip.sha256')).read_text(encoding='utf-8').split()[0]
 if hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()!=expected:
  raise ValueError('Empreinte du paquet incorrecte ; télécharger une copie intacte.')
 destination=destination.expanduser().resolve()
 plugin=destination/'plugins/vaeltharyn-translator'
 with zipfile.ZipFile(ARCHIVE) as archive:
  entries=archive.infolist()
  for entry in entries:
   path=PurePosixPath(entry.filename)
   if path.is_absolute() or '..' in path.parts or '\\' in entry.filename or ':' in entry.filename or stat.S_ISLNK(entry.external_attr>>16):
    raise ValueError('Chemin non autorisé dans le paquet : '+entry.filename)
  manifest=json.loads(archive.read('plugin.json'))
  if manifest['name']!='vaeltharyn-translator' or manifest['version']!=VERSION:
   raise ValueError('Identité ou version inattendue dans le paquet.')
  # An existing installation is accepted only if every packaged file is identical.
  # A different file is never silently overwritten.
  for entry in entries:
   target=plugin/entry.filename
   if target.exists() and not entry.is_dir():
    if not target.is_file() or target.read_bytes()!=archive.read(entry):
     raise ValueError('Fichier différent déjà présent : '+str(target)+' ; choisir un autre dossier.')
  catalog=destination/'.agents/plugins/marketplace.json'
  data={'name':'vaeltharyn','interface':{'displayName':'Vaeltharyn'},'plugins':[{'name':'vaeltharyn-translator','source':{'source':'local','path':'./plugins/vaeltharyn-translator'},'policy':{'installation':'AVAILABLE','authentication':'ON_INSTALL'},'category':'Productivity'}]}
  if catalog.exists() and json.loads(catalog.read_text(encoding='utf-8'))!=data:
   raise ValueError('Un autre catalogue existe dans ce dossier ; choisir un dossier dédié.')
  plugin.mkdir(parents=True,exist_ok=True)
  archive.extractall(plugin)
  catalog.parent.mkdir(parents=True,exist_ok=True)
  catalog.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 return destination

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--destination',type=Path,default=ROOT/'dist'/f'vaeltharyn-{VERSION}',help='Dossier dédié au catalogue ; défaut : dist/vaeltharyn-<version> dans le dépôt')
 args=parser.parse_args()
 try:destination=prepare(args.destination)
 except (OSError,ValueError,KeyError,zipfile.BadZipFile) as exc:parser.exit(2,str(exc)+'\n')
 print(f'Plugin {VERSION} préparé dans : {destination}')
 print('Pour l’installer dans Codex :')
 print(f'codex plugin marketplace add "{destination}"')
 print('codex plugin add vaeltharyn-translator@vaeltharyn')

if __name__=='__main__':main()
