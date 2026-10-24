"""Checks the bilingual expressive supplement without third-party dependencies.
Optional --baseline validates preservation against an existing Git revision.
"""
from pathlib import Path
from collections import Counter
import csv,io,json,re,subprocess,argparse
P=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--baseline');args=ap.parse_args()
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f,delimiter=';'))
fr=read(P/'lexique_detaille.csv');en=read(P/'en/lexique_detaille.csv')
fs=read(P/'lexique.csv');es=read(P/'en/lexique.csv')
assert len(fr)==len(en)==len(fs)==len(es)==65017
assert len({r['mot'] for r in fr})==65014
assert [(r['mot'],r['categorie'],r['id']) for r in fr]==[(r['word'],r['category'],r['id']) for r in en]
assert len({r['id'] for r in fr})==len(fr)
if args.baseline:
 for filename,current in [('lexique.csv',fs),('lexique_detaille.csv',fr),('en/lexique.csv',es),('en/lexique_detaille.csv',en)]:
  blob=subprocess.run(['git','show',args.baseline+':'+filename],cwd=P,check=True,stdout=subprocess.PIPE).stdout.decode('utf-8-sig')
  old=list(csv.DictReader(io.StringIO(blob),delimiter=';'))
  assert len(old)==65007 and current[:len(old)]==old,filename
new=json.loads((P/'registres/entrees_nouvelles.json').read_text(encoding='utf-8'))
expressions=json.loads((P/'registres/expressions.json').read_text(encoding='utf-8'))
assert len(new)==10 and len(expressions)==79
frmap={(x['mot'],x['categorie']):x for x in fr};enmap={(x['word'],x['category']):x for x in en}
for item in new:
 x=item['fr'];y=item['en'];k=(x['mot'],x['categorie'])
 assert x==frmap[k] and y==enmap[k]
 assert x['id']==y['id'] and x['api']==y['ipa']
 assert 'NON VALIDÉE' in x['statut'] and 'UNVALIDATED' in y['status']
 assert x['definition_fr']==y['definition_fr_source'] and x['definition_fr'] and y['definition_en']
 if x['categorie']=='v':assert x['valence']==y['valency']=='intr'
assert {x['mot'] for x in fr[65007:]}=={'sketh','grusk','gruskar','vrask','skarn','skarnar','grusk-tharel','graeth-naelkaror'}

# Build lexical analyses, rather than merely checking that words look plausible.
def forms(x):
 w=x['mot'];c=x['categorie'];yield w
 if c=='n':
  for n in ('','i'):
   for case in ('','en','or','ath','ul'):yield w+n+case
 elif c=='v':
  for pre in ('','ra','vi'):
   for mode in ('','ir','el'):
    for ending in ('em','es','e','om','os','en'):yield pre+w[:-2]+mode+ending
  for ending in ('a','ai','in','eth','or','el'):yield w[:-2]+ending
  if x['valence'].startswith('tr'):yield w[:-2]+'un'
 elif c=='adj':yield w+'is';yield w+'eth'
allowed=set()
for x in fr:allowed.update(forms(x))
allowed.update(p+'-'+c for p in ('mi','ti','se','min','tin','sen','si') for c in ('en','or','ath','ul'))
oldwords={r['mot'] for r in fr[:65007]}
oldforms=set()
for x in fr[:65007]:oldforms.update(forms(x))
assert not ({x['mot'] for x in fr[65007:]} & oldforms), 'New lemma collides with an older form'
for x in fr[65007:]:
 if x['categorie']=='v':assert not (set(forms(x)) & oldwords),'New verb form collides with an older lemma'
for e in expressions:
 tokens=re.findall(r'[a-záéíóúý]+(?:-[a-záéíóúý]+)*',e['vaeltharyn'].lower())
 assert set(tokens)<=allowed,(e['id'],set(tokens)-allowed)
 assert e['francais'] and e['english'] and e['litteral_fr'] and e['literal_en']
 assert 0<=e['intensite']<=4
 assert not re.search(r'\bTi (?:nu )?vele\b',e['vaeltharyn']),'2SG copula must be veles'
assert len({e['id'] for e in expressions})==len(expressions)
assert len({e['vaeltharyn'] for e in expressions})==len(expressions)
byid={e['id']:e for e in expressions}
aliases=read(P/'registres/renvois_fr_en.csv')
for x in aliases:assert byid[x['id_expression']]['vaeltharyn']==x['expression']
for doc in [P/'23_Jurons_insultes_expressions.md',P/'en/23_Jurons_insultes_expressions.md']:
 text=doc.read_text(encoding='utf-8')
 for e in expressions:assert e['id'] in text and e['vaeltharyn'] in text
 for x in new:assert x['fr']['id'] in text
 from urllib.parse import unquote,urlsplit
 for link in re.findall(r'\]\(([^)]+)\)',text):
  if urlsplit(link).scheme:continue
  assert (doc.parent/unquote(link.split('#')[0])).is_file(),link
report={'entries':len(fr),'distinct_spellings':len({r['mot'] for r in fr}),'new_lexical_entries':len(new),'expressions':len(expressions),'lookup_aliases':len(aliases),'old_entries_preserved':65007 if args.baseline else 'not checked without --baseline','fr_en_alignment':'pass','lexical_and_morphological_coverage':'pass','older_lemma_collisions':'none','status':'written checks; no audio or creator validation claimed'}
print(json.dumps(report,ensure_ascii=False,indent=2))
