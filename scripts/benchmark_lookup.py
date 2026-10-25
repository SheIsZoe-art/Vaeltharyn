"""Reproducible lexical exact-lookup benchmark without historical Git dependencies."""
from pathlib import Path
from contextlib import closing
import argparse,json,os,statistics,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from vaeltharyn.resources import manifest
from vaeltharyn.search import connect,lookup,norm,rows
def query(lang,terms,linear):
    if not linear:
        result=lookup(ROOT,lang,terms,100)
        return {term:sorted(r['id'] for r in result['results'][term]['entries']) for term in terms}
    m=manifest(ROOT);path=m['lexicon']['en' if lang=='en' else 'fr']['detailed'];result={term:[] for term in terms}
    for row in rows(ROOT/path):
        values=[row['mot']] if lang=='vh' else [row['english_headword'],row['meaning']] if lang=='en' else [row['francais'],row['sens']]
        for term in terms:
            if any(norm(term)==norm(value) for value in values if value):result[term].append(row['id'])
    return {term:sorted(values) for term,values in result.items()}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--query',action='store_true');p.add_argument('--linear',action='store_true');p.add_argument('--lang');p.add_argument('terms',nargs='*');a=p.parse_args()
    if a.query:print(json.dumps(query(a.lang,a.terms,a.linear)));return
    with closing(connect(ROOT,manifest(ROOT))):pass
    env=dict(os.environ);env.pop('VAELTHARYN_ROOT',None);results=[]
    for lang,terms in [('fr',['faim','colère']),('en',['synthesizer','harmonic frequency','badass','exchange for mine']),('vh',['saevron','haem'])]:
        timing={};answers={}
        for mode in ('linear','indexed'):
            values=[]
            args=[sys.executable,str(Path(__file__).resolve()),'--query','--lang',lang,*(['--linear'] if mode=='linear' else []),*terms]
            for n in range(4):
                start=time.perf_counter();output=subprocess.check_output(args,env=env,cwd=ROOT);elapsed=time.perf_counter()-start
                if n:values.append(elapsed)
                answers[mode]=json.loads(output)
            timing[mode]=round(statistics.median(values)*1000,2)
        assert answers['linear']==answers['indexed']
        results.append({'lang':lang,'terms':terms,'median_ms':timing,'speedup':round(timing['linear']/timing['indexed'],1)})
    report={'method':'Exact lexical candidate IDs; full CLI wall time including Python startup, one warm-up and three measured runs. Indexed lookup also consults expression registries. Same source inputs; no historical Git objects required. Local timings, not a universal guarantee.','structure_version':manifest(ROOT)['structure_version'],'results':results}
    (ROOT/'docs/quality').mkdir(exist_ok=True);(ROOT/'docs/quality/lookup-benchmark.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
