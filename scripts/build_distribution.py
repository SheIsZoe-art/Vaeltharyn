"""Build standalone plugin and skill archives from the current source corpus."""
import hashlib,json,os,re,shutil,sys,urllib.parse,zipfile
from pathlib import Path
from contextlib import closing
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from vaeltharyn.resources import manifest
from vaeltharyn.search import connect

VERSION='0.5.0'
OUTPUT=ROOT/'distributions'
STAGE=ROOT/'dist/build-0.5.0'
BRANCH='https://github.com/SheIsZoe-art/Vaeltharyn/blob/feat/jurons-insultes-fr-en/'

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def snapshot(skill,index):
    target=skill/'references/corpus';target.mkdir(parents=True,exist_ok=True)
    m=manifest(ROOT)
    m['distribution']={'format':'indexed','index':'data/search.sqlite3','index_schema_version':1,'index_sha256':digest(index)}
    # CSV paths still identify the authoritative source; storage is the indexed snapshot.
    m['distribution']['authoritative_source']='https://github.com/SheIsZoe-art/Vaeltharyn/tree/feat/jurons-insultes-fr-en'
    (target/'corpus.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    shutil.copytree(ROOT/'docs',target/'docs')
    shutil.copytree(ROOT/'data/expressions',target/'data/expressions')
    (target/'archives').mkdir();shutil.copy2(ROOT/'archives/legacy-paths.json',target/'archives/legacy-paths.json')
    shutil.copy2(ROOT/'LICENSE.md',target/'LICENSE.md')
    shutil.copy2(index,target/'data/search.sqlite3')
    shutil.copytree(ROOT/'vaeltharyn',skill/'scripts/vaeltharyn',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    # Keep useful links in the lean package: omitted source material resolves to GitHub.
    def rewrite(match,doc):
        text=match.group(1);parsed=urllib.parse.urlsplit(text.strip('<>'))
        if parsed.scheme or parsed.netloc or not parsed.path:return match.group(0)
        dest=(doc.parent/urllib.parse.unquote(parsed.path)).resolve()
        if not dest.is_relative_to(target.resolve()) or dest.exists():return match.group(0)
        rel=dest.relative_to(target.resolve()).as_posix()
        return ']('+BRANCH+urllib.parse.quote(rel,safe='/._-~')+('#'+parsed.fragment if parsed.fragment else '')+')'
    for doc in target.rglob('*.md'):
        doc.write_text(re.sub(r'\]\(([^)\n]+)\)',lambda match:rewrite(match,doc),doc.read_text(encoding='utf-8')),encoding='utf-8')
    if digest(target/'data/search.sqlite3')!=m['distribution']['index_sha256']:raise ValueError('Snapshot index changed')

def archive(source,name):
    output=OUTPUT/name
    with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for path in sorted(source.rglob('*')):
            if not path.is_file() or '__pycache__' in path.parts or path.suffix=='.pyc':continue
            info=zipfile.ZipInfo(path.relative_to(source).as_posix(),date_time=(2026,10,25,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
            z.writestr(info,path.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    if output.stat().st_size>=100_000_000:raise ValueError('Archive exceeds GitHub file limit')
    output.with_suffix('.zip.sha256').write_text(digest(output)+'  '+output.name+'\n',encoding='utf-8')
    return {'file':output.name,'sha256':digest(output),'bytes':output.stat().st_size}

def main():
    OUTPUT.mkdir(exist_ok=True)
    if STAGE.exists():
        assert STAGE.resolve().is_relative_to((ROOT/'dist').resolve())
        shutil.rmtree(STAGE)
    STAGE.mkdir(parents=True)
    with closing(connect(ROOT,manifest(ROOT))) as db:
        index=ROOT/'.cache/search.sqlite3'
        counts={k:json.loads(v) for k,v in db.execute("SELECT key,value FROM meta WHERE key IN ('entries','expressions','corpus_version')")}
    plugin=STAGE/'plugin';shutil.copytree(ROOT/'integrations/plugin',plugin)
    skill=STAGE/'skill';shutil.copytree(ROOT/'integrations/skill',skill)
    snapshot(plugin/'skills/translate-vaeltharyn',index);snapshot(skill,index)
    report={'plugin_version':VERSION,'corpus_version':'1.5.0','structure_version':'2.0.0','creator':'SheIsZoe','counts':counts,'index_bytes':index.stat().st_size,'plugin':archive(plugin,f'vaeltharyn-translator-{VERSION}.zip'),'skill':archive(skill,'vaeltharyn-skill-1.5.0-structure-2.0.0.zip')}
    (OUTPUT/'latest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
