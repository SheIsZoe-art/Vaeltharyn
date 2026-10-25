"""Recherche FR/EN/Vaeltharyn en lecture seule, entrées et expressions contextualisées."""
import argparse,csv,json,os,sys,unicodedata
from pathlib import Path

LIVE=Path.home()/'Documents/ChatGPT/Vaeltharyn/publication-github'
REPO=Path(__file__).resolve().parents[1]
SNAPSHOT=Path(__file__).resolve().parents[1]/'references/corpus'
def norm(s):
 return ' '.join(unicodedata.normalize('NFC',s).casefold().replace('’',"'").strip(' \t\r\n!?.,;').split())
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('terms',nargs='+');p.add_argument('--lang',choices=['fr','en','vh'],required=True)
 p.add_argument('--root',type=Path);p.add_argument('--contains',action='store_true');p.add_argument('--limit',type=int,default=12)
 a=p.parse_args()
 if a.limit<1:p.error('--limit doit être positif')
 root=a.root or (Path(os.environ['VAELTHARYN_ROOT']) if os.environ.get('VAELTHARYN_ROOT') else LIVE if LIVE.is_dir() else REPO if (REPO/'lexique_detaille.csv').is_file() else SNAPSHOT)
 results={t:{'total':0,'entries':[],'expression_total':0,'expressions':[]} for t in a.terms}
 def match(t,values):return any(norm(t) in norm(v) if a.contains else norm(t)==norm(v) for v in values if v)
 try:
  filename=root/('en/lexique_detaille.csv' if a.lang=='en' else 'lexique_detaille.csv')
  with filename.open(encoding='utf-8-sig',newline='') as f:
   for row in csv.DictReader(f,delimiter=';'):
    fields=([row['mot']] if a.lang=='vh' else [row['english_headword'],row['meaning']] if a.lang=='en' else [row['francais'],row['sens']])
    if a.contains:fields.append(row.get('definition_en' if a.lang=='en' else 'definition_fr',''))
    for t,r in results.items():
     if match(t,fields):
      r['total']+=1
      if len(r['entries'])<a.limit:r['entries'].append({k:v for k,v in row.items() if v})
  folder=root/'registres/inventaire-2026-10-25'
  senses=json.loads((folder/'sens.json').read_text(encoding='utf-8'))
  routes=json.loads((folder/'couverture.json').read_text(encoding='utf-8'))
  originals={s['key']:[] for s in senses}
  for row in routes:
   if row['langue']==a.lang:
    for key in row['sens_cles']:originals[key].append({'id':row['id'],'source':row['source'],'provided_correspondence':row['correspondance_fournie'],'note_fr':row['note_fr'],'note_en':row['note_en']})
  editions=['1.4.0']
  for supplement in sorted((root/'complements').glob('*/sens.json')):
   for s in json.loads(supplement.read_text(encoding='utf-8')):
    senses.append({**s,'fichier_complement':supplement.relative_to(root).as_posix()})
   bilan=supplement.parent/'bilan.json'
   if bilan.is_file():editions.append(json.loads(bilan.read_text(encoding='utf-8'))['version'])
  for s in senses:
   source_rows=[] if s.get('fichier_complement') else originals[s['key']]
   fields=[s['vaeltharyn']] if a.lang=='vh' else [s['english_checked' if a.lang=='en' else 'francais_controle']]+[r['source'] for r in source_rows]+s.get('aliases_'+a.lang,[])
   if a.lang=='en' and s.get('source_en'):fields.append(s['source_en'])
   if a.contains:fields.append(s['note_en' if a.lang=='en' else 'note_fr'])
   for t,r in results.items():
    if match(t,fields):
     r['expression_total']+=1
     if len(r['expressions'])<a.limit:r['expressions'].append({**s,'source_matches':[x for x in source_rows if match(t,[x['source']])]})
  # Preserve access to the first 79 expressions, including forms absent from the extension.
  for s in json.loads((root/'registres/expressions.json').read_text(encoding='utf-8')):
   field={'fr':'francais','en':'english','vh':'vaeltharyn'}[a.lang]
   for t,r in results.items():
    if match(t,[s[field]]) and not any(x.get('expression_id',x.get('id'))==s['id'] for x in r['expressions']):
     r['expression_total']+=1
     if len(r['expressions'])<a.limit:r['expressions'].append(s)
 except (OSError,KeyError,ValueError,csv.Error) as e:p.exit(2,f'Corpus incomplet ou illisible : {e}\n')
 print(json.dumps({'corpus_root':str(root),'edition':max(editions,key=lambda v:tuple(map(int,v.split('.')))),'results':results},ensure_ascii=False,indent=2))
if __name__=='__main__':
 if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
 main()
