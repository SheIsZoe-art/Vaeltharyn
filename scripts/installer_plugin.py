"""Download the current verified release and prepare a dedicated local marketplace."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,os,stat,urllib.request,zipfile
ROOT=Path(__file__).resolve().parents[1]
LATEST=json.loads((ROOT/'integrations/release.json').read_text(encoding='utf-8'));VERSION=LATEST['plugin_version']
def digest(path):
    with path.open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()
def acquire(explicit=None):
    if explicit:path=Path(explicit).resolve()
    else:
        built=ROOT/'dist/releases'/LATEST['plugin']['file']
        path=built if built.is_file() else ROOT/'.cache/downloads'/LATEST['plugin']['file']
        if not path.exists():
            path.parent.mkdir(parents=True,exist_ok=True);temp=path.with_suffix('.download')
            try:
                with urllib.request.urlopen(LATEST['plugin']['url'],timeout=60) as response,temp.open('wb') as output:
                    while chunk:=response.read(1024*1024):output.write(chunk)
                if digest(temp)!=LATEST['plugin']['sha256']:raise ValueError('Downloaded package hash mismatch')
                os.replace(temp,path)
            finally:
                if temp.exists():temp.unlink()
    if digest(path)!=LATEST['plugin']['sha256']:raise ValueError('Package hash mismatch; use an intact release archive')
    return path
def prepare(destination,archive_path=None):
    archive_path=acquire(archive_path);destination=destination.expanduser().resolve();plugin=destination/'plugins/vaeltharyn-translator'
    with zipfile.ZipFile(archive_path) as z:
        entries=z.infolist()
        for entry in entries:
            path=PurePosixPath(entry.filename)
            if path.is_absolute() or '..' in path.parts or '\\' in entry.filename or ':' in entry.filename or stat.S_ISLNK(entry.external_attr>>16):raise ValueError('Invalid archive path')
        m=json.loads(z.read('plugin.json'))
        if m['name']!='vaeltharyn-translator' or m['version']!=VERSION:raise ValueError('Unexpected package identity')
        for entry in entries:
            target=plugin/entry.filename
            if target.exists() and not entry.is_dir() and (not target.is_file() or target.read_bytes()!=z.read(entry)):raise ValueError('Different local file: '+str(target)+'; choose a new destination')
        catalog=destination/'.agents/plugins/marketplace.json'
        data={'name':'vaeltharyn','interface':{'displayName':'Vaeltharyn'},'plugins':[{'name':'vaeltharyn-translator','source':{'source':'local','path':'./plugins/vaeltharyn-translator'},'policy':{'installation':'AVAILABLE','authentication':'ON_INSTALL'},'category':'Productivity'}]}
        if catalog.exists() and json.loads(catalog.read_text(encoding='utf-8'))!=data:raise ValueError('A different marketplace already exists')
        plugin.mkdir(parents=True,exist_ok=True);z.extractall(plugin);catalog.parent.mkdir(parents=True,exist_ok=True)
        catalog.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return destination
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--destination',type=Path,default=ROOT/'dist'/('vaeltharyn-'+VERSION));p.add_argument('--archive',type=Path);a=p.parse_args()
    try:dest=prepare(a.destination,a.archive)
    except (OSError,ValueError,KeyError,zipfile.BadZipFile) as error:p.exit(2,str(error)+'\n')
    print('Prepared plugin '+VERSION+' in '+str(dest));print('codex plugin marketplace add "'+str(dest)+'"');print('codex plugin add vaeltharyn-translator@vaeltharyn')
if __name__=='__main__':main()
