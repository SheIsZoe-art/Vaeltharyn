"""Build portable releases from canonical sources; generated binaries stay outside Git."""
from pathlib import Path
from contextlib import closing
import hashlib,json,posixpath,re,shutil,sys,urllib.parse,zipfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from vaeltharyn.resources import manifest
from vaeltharyn.search import connect,SCHEMA
PLUGIN=json.loads((ROOT/'integrations/plugin/plugin.json').read_text(encoding='utf-8'))
VERSION=PLUGIN['version'];OUTPUT=ROOT/'dist/releases';STAGE=ROOT/'dist'/('build-'+VERSION)
SOURCE='https://github.com/SheIsZoe-art/Vaeltharyn'
DOWNLOAD=SOURCE+'/releases/download/v'+VERSION+'/'
def digest(path):
    with path.open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()
def snapshot(skill,index):
    target=skill/'references/corpus';target.mkdir(parents=True,exist_ok=True)
    m=manifest(ROOT);m['distribution']={'format':'indexed','index':'data/search.sqlite3','index_schema_version':SCHEMA,'index_sha256':digest(index),'authoritative_source':SOURCE+'/tree/main'}
    (target/'corpus.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for name in m['packaged_documents']:
        source=(ROOT/name).resolve();destination=target/name
        if not source.is_relative_to((ROOT/'docs').resolve()):raise ValueError('Document outside the canonical reference')
        destination.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,destination)
    (target/'data/provenance').mkdir(parents=True,exist_ok=True)
    for name in ('integrity.json','NOTICE.md','references.json'):shutil.copy2(ROOT/'data/provenance'/name,target/'data/provenance'/name)
    shutil.copy2(ROOT/'LICENSE.md',target/'LICENSE.md');shutil.copy2(index,target/'data/search.sqlite3')
    shutil.copytree(ROOT/'vaeltharyn',skill/'scripts/vaeltharyn',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    edition={'corpus_version':m['corpus_version'],'structure_version':m['structure_version'],'plugin_version':VERSION,'creator':'SheIsZoe','source':SOURCE+'/tree/main','source_integrity_sha256':digest(ROOT/'data/provenance/integrity.json'),'format':'indexed'}
    (skill/'references/edition.json').write_text(json.dumps(edition,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    def rewrite(match,doc):
        raw=match.group(1);u=urllib.parse.urlsplit(raw.strip('<>'))
        if u.scheme or u.netloc or not u.path:return match.group(0)
        dest=(doc.parent/urllib.parse.unquote(u.path)).resolve()
        if not dest.is_relative_to(target.resolve()) or dest.exists():return match.group(0)
        return ']('+SOURCE+'/blob/main/'+urllib.parse.quote(dest.relative_to(target.resolve()).as_posix(),safe='/._-~')+('#'+u.fragment if u.fragment else '')+')'
    for doc in target.rglob('*.md'):
        doc.write_bytes(re.sub(r'\]\(([^)\n]+)\)',lambda match:rewrite(match,doc),doc.read_text(encoding='utf-8')).encode('utf-8'))
    assert digest(target/'data/search.sqlite3')==m['distribution']['index_sha256']
def archive(source,name):
    output=OUTPUT/name
    with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for path in sorted(source.rglob('*')):
            if not path.is_file() or '__pycache__' in path.parts or path.suffix=='.pyc':continue
            info=zipfile.ZipInfo(path.relative_to(source).as_posix(),date_time=(2026,10,25,0,0,0));info.external_attr=0o100644<<16
            z.writestr(info,path.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    sha=digest(output);output.with_suffix('.zip.sha256').write_text(sha+'  '+name+'\n',encoding='utf-8')
    return {'file':name,'sha256':sha,'bytes':output.stat().st_size,'url':DOWNLOAD+name}
def main():
    OUTPUT.mkdir(parents=True,exist_ok=True)
    if STAGE.exists():
        assert STAGE.resolve().is_relative_to((ROOT/'dist').resolve());shutil.rmtree(STAGE)
    STAGE.mkdir(parents=True)
    with closing(connect(ROOT,manifest(ROOT))) as db:
        index=ROOT/'.cache/search.sqlite3'
        counts={k:json.loads(v) for k,v in db.execute("SELECT key,value FROM meta WHERE key IN ('entries','expressions','corpus_version')")}
    plugin=STAGE/'plugin';shutil.copytree(ROOT/'integrations/plugin',plugin)
    standalone=STAGE/'skill';shutil.copytree(ROOT/'integrations/skill',standalone)
    embedded=plugin/'skills/translate-vaeltharyn';shutil.copytree(ROOT/'integrations/skill',embedded)
    for path in [embedded/'SKILL.md',embedded/'agents/openai.yaml']:
        path.write_bytes(path.read_text(encoding='utf-8').replace('vaeltharyn-traducteur','translate-vaeltharyn').encode('utf-8'))
    overlay={k:v for k,v in PLUGIN.items() if k not in ('$schema','extensions')}
    overlay['interface']=PLUGIN['extensions']['com.openai']['interface'];overlay['skills']='./skills'
    (plugin/'.codex-plugin').mkdir();(plugin/'.codex-plugin/plugin.json').write_text(json.dumps(overlay,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    snapshot(embedded,index);snapshot(standalone,index)
    m=manifest(ROOT)
    report={'plugin_version':VERSION,'corpus_version':m['corpus_version'],'structure_version':m['structure_version'],'creator':'SheIsZoe','tag':'v'+VERSION,'release_url':SOURCE+'/releases/tag/v'+VERSION,'counts':counts,'index_bytes':index.stat().st_size,'plugin':archive(plugin,'vaeltharyn-translator-'+VERSION+'.zip'),'skill':archive(standalone,'vaeltharyn-skill-'+VERSION+'.zip')}
    (ROOT/'integrations/release.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (OUTPUT/'release.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
