"""Verify portable packages, installer behavior, provenance and lookup."""
from pathlib import Path,PurePosixPath
from contextlib import closing
import hashlib,json,os,sqlite3,subprocess,sys,tempfile,zipfile
ROOT=Path(__file__).resolve().parents[1]

def run(script,*args,cwd=None,success=True):
    env=dict(os.environ);env.pop('VAELTHARYN_ROOT',None)
    r=subprocess.run([sys.executable,'-X','utf8',str(script),*map(str,args)],cwd=cwd,env=env,capture_output=True,encoding='utf-8')
    assert (r.returncode==0)==success,(r.returncode,r.stderr)
    return r.stdout

def verify_skill(skill,cwd):
    corpus=skill/'references/corpus';m=json.loads((corpus/'corpus.json').read_text(encoding='utf-8'))
    assert m['corpus_version']=='1.5.0' and m['distribution']['format']=='indexed'
    index=corpus/m['distribution']['index']
    assert hashlib.sha256(index.read_bytes()).hexdigest()==m['distribution']['index_sha256']
    assert not list(corpus.rglob('entries.csv'))
    with closing(sqlite3.connect(index.resolve().as_uri()+'?mode=ro',uri=True)) as db:
        assert db.execute('PRAGMA quick_check').fetchone()[0]=='ok'
        assert db.execute("SELECT count(*) FROM records WHERE kind='entry'").fetchone()[0]==65041
        assert db.execute("SELECT count(*) FROM records WHERE kind='expression'").fetchone()[0]==416
        raw=db.execute("SELECT payload FROM records WHERE kind='expression'").fetchall()
        assert sum(len(json.loads(x[0]).get('source_routes',[])) for x in raw)>=719
    script=skill/'scripts/chercher.py'
    result=json.loads(run(script,'--lang','en','harmonic frequency','exchange for mine',cwd=cwd))
    assert Path(result['corpus_root']).resolve()==corpus.resolve()
    assert result['results']['harmonic frequency']['expressions'][0]['vaeltharyn']=='korthir goesumen'
    assert result['results']['exchange for mine']['expressions'][0]['schema_a_completer']
    fr=json.loads(run(script,'--lang','fr','faim',cwd=cwd))
    assert fr['results']['faim']['entries'][0]['word']=='haem'
    senses=json.loads(run(script,'--lang','vh','Thalen moelom!',cwd=cwd))
    assert {'weird_warning','unusual'}<={r.get('key') for r in senses['results']['Thalen moelom!']['expressions']}
    run(script,'--root',cwd/'missing-corpus','--lang','fr','faim',cwd=cwd,success=False)
    run(script,'--lang','fr','faim','--limit','101',cwd=cwd,success=False)
    return result

def main():
    latest=json.loads((ROOT/'distributions/latest.json').read_text(encoding='utf-8'))
    (ROOT/'dist').mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='verification-',dir=ROOT/'dist') as temp:
        temp=Path(temp);assert temp.resolve().is_relative_to((ROOT/'dist').resolve())
        for kind in ('plugin','skill'):
            archive=ROOT/'distributions'/latest[kind]['file']
            assert hashlib.sha256(archive.read_bytes()).hexdigest()==latest[kind]['sha256']
            assert archive.stat().st_size<100_000_000
            with zipfile.ZipFile(archive) as z:
                assert z.testzip() is None
                for info in z.infolist():
                    path=PurePosixPath(info.filename)
                    assert not path.is_absolute() and '..' not in path.parts and '\\' not in info.filename and ':' not in info.filename
                    assert not ('__pycache__' in path.parts or info.filename.endswith('.pyc'))
                    if info.filename.endswith(('.md','.json','.yaml','.py')):
                        content=z.read(info)
                        assert b'C:/Users/user/' not in content and b'C:\\Users\\user\\' not in content,info.filename
                z.extractall(temp/kind)
        plugin=temp/'plugin'
        a=json.loads((plugin/'plugin.json').read_text(encoding='utf-8'));b=json.loads((plugin/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))
        assert a['name']==b['name']=='vaeltharyn-translator'
        assert a['version']==b['version']==latest['plugin_version']=='0.5.0'
        assert a['author']['name']==b['author']['name']=='SheIsZoe'
        assert a['extensions']['com.openai']['interface']==b['interface']
        assert b['interface']['developerName']=='SheIsZoe'
        assert b['interface']['defaultPrompt']=='Traduis ce passage en Vaeltharyn en respectant les formes canoniques et en signalant les mots incertains.'
        x=verify_skill(plugin/'skills/translate-vaeltharyn',temp)
        y=verify_skill(temp/'skill',temp)
        assert x['results']==y['results']
        destination=temp/'catalogue avec espaces'
        for repeat in range(2):run(ROOT/'scripts/installer_plugin.py','--destination',destination,cwd=temp)
        catalog=json.loads((destination/'.agents/plugins/marketplace.json').read_text(encoding='utf-8'))
        installed=destination/catalog['plugins'][0]['source']['path']
        assert json.loads((installed/'plugin.json').read_text(encoding='utf-8'))['version']=='0.5.0'
        (installed/'README.md').write_text('Changed local source',encoding='utf-8')
        run(ROOT/'scripts/installer_plugin.py','--destination',destination,cwd=temp,success=False)
    report={'status':'pass','plugin_version':'0.5.0','corpus_version':'1.5.0','creator':'SheIsZoe','independent_snapshot_lookup':'pass','bilingual_records':65041,'expression_records':416,'hashes_and_archive_integrity':'pass','explicit_invalid_root_rejected':True,'installer_idempotence_and_overwrite_protection':'pass','identity_and_default_prompt_preserved':True}
    (ROOT/'distributions/verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
