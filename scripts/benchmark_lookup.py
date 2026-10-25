"""Compare warm CLI lookups with the pre-refactor linear scanner, on this machine."""
from pathlib import Path
from contextlib import closing
import json,shutil,statistics,subprocess,sys,tempfile,time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from vaeltharyn.search import connect
from vaeltharyn.resources import manifest

def main():
    with closing(connect(ROOT,manifest(ROOT))):pass
    (ROOT/'dist').mkdir(exist_ok=True)
    tests=[('fr',['faim','colère']),('en',['synthesizer','harmonic frequency','badass','exchange for mine']),('vh',['saevron','haem'])]
    results=[]
    with tempfile.TemporaryDirectory(prefix='benchmark-',dir=ROOT/'dist') as temp:
        folder=Path(temp);assert folder.resolve().is_relative_to((ROOT/'dist').resolve())
        old=folder/'chercher-old.py';old.write_bytes(subprocess.check_output(['git','show','90cbfb4:scripts/chercher_corpus.py'],cwd=ROOT))
        aliases=json.loads((ROOT/'archives/legacy-paths.json').read_text(encoding='utf-8'))['files']
        legacy=folder/'legacy'
        for before,after in aliases.items():
            if not after.startswith('data/'):continue
            dest=legacy/before;dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(ROOT/after,dest)
        for lang,terms in tests:
            times={'linear':[],'indexed':[]};outputs={};sizes={}
            for label,script,root in [('linear',old,legacy),('indexed',ROOT/'scripts/chercher_corpus.py',ROOT)]:
                for repeat in range(4):
                    start=time.perf_counter()
                    raw=subprocess.check_output([sys.executable,'-X','utf8',str(script),'--root',str(root),'--lang',lang,'--limit','100',*terms],cwd=folder)
                    elapsed=time.perf_counter()-start
                    if repeat:times[label].append(elapsed)
                    outputs[label]=json.loads(raw);sizes[label]=len(raw)
            for term in terms:
                a=outputs['linear']['results'][term];b=outputs['indexed']['results'][term]
                assert {r['id'] for r in a['entries']}=={r['id'] for r in b['entries']},term
                def identities(records):return {r.get('expression_id') or r.get('id') or r.get('key') for r in records}
                assert identities(a['expressions'])<=identities(b['expressions']),term
            medians={key:round(statistics.median(values)*1000,2) for key,values in times.items()}
            results.append({'lang':lang,'terms':terms,'median_ms':medians,'speedup':round(medians['linear']/medians['indexed'],1),'output_bytes':sizes})
    report={'method':'CLI wall time including Python startup; one warm-up and three measured runs; same source data; local machine, not a universal guarantee','baseline':'90cbfb4','indexed_version':'2.0.0','results':results}
    (ROOT/'distributions/benchmark.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
