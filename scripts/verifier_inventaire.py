"""Independent preservation, coverage, morphology and reference checks for 1.4.0."""
from pathlib import Path
import sys
from urllib.parse import unquote
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from vaeltharyn.resources import legacy_path
import csv,io,json,re,hashlib,subprocess,collections
P=Path(__file__).resolve().parents[1]
A=legacy_path(P,'registres/inventaire-2026-10-25')
def js(p):return json.loads(p.read_text(encoding='utf-8'))
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f,delimiter=';'))
fr=read(legacy_path(P,'lexique_detaille.csv'));en=read(legacy_path(P,'en/lexique_detaille.csv'))
for name in ['lexique.csv','lexique_detaille.csv','en/lexique.csv','en/lexique_detaille.csv']:
 current=read(legacy_path(P,name))
 blob=subprocess.run(['git','show','cbd0428:'+name],cwd=P,check=True,stdout=subprocess.PIPE).stdout
 old=list(csv.DictReader(io.StringIO(blob.decode('utf-8-sig')),delimiter=';'))
 assert len(old)==65017 and current[:65017]==old,name
 assert len(current)>=65026,name
assert len({r['mot'] for r in fr})>=65023
assert sum(r['categorie']=='v' for r in fr)==6538
assert [(r['mot'],r['categorie'],r['id']) for r in fr]==[(r['word'],r['category'],r['id']) for r in en]
assert len({r['id'] for r in fr})==len(fr)
byword={r['mot']:r for r in fr}
new=js(A/'entrees_nouvelles.json');assert len(new)==9
for n in new:
 x=n['fr'];y=n['en']
 assert x==byword[x['mot']] and y==en[fr.index(x)]
 assert 'NON VALIDÉE' in x['statut'] and 'UNVALIDATED' in y['status']
 assert x['definition_fr']==y['definition_fr_source'] and x['api']==y['ipa']
 for b in x['base'].split(' + '):assert byword[b]['categorie']=='n'
def forms(x):
 w=x['mot'];yield w
 if x['categorie']=='n':
  for suffix in ('','il','aun'):
   for plural in ('','i'):
    for case in ('','en','or','ath','ul'):yield w+suffix+plural+case
 elif x['categorie']=='v':
  st=w[:-2]
  for prefix in ('','ra','vi'):
   for mood in ('','ir','el'):
    for ending in ('em','es','e','om','os','en'):yield prefix+st+mood+ending
  for suffix in ('a','ai','in','or','el'):yield st+suffix
  if x['valence'].startswith('tr'):yield st+'un'
  for plural in ('','i'):
   for case in ('','en','or','ath','ul'):yield st+'eth'+plural+case
 elif x['categorie']=='adj':yield w+'is';yield w+'eth'
oldforms=set();allowed=set()
for x in fr[:65017]:oldforms.update(forms(x))
for x in fr:allowed.update(forms(x))
oldlemmas={x['mot'] for x in fr[:65017]}
assert not ({x['mot'] for x in fr[65017:]} & oldforms),'New lemma collision'
for x in fr[65017:]:
 if x['categorie']=='v':assert not (set(forms(x)) & oldlemmas),x['mot']
allowed.update(p+'-'+c for p in ('mi','ti','se','min','tin','sen','si') for c in ('en','or','ath','ul'))
allowed.add('sherlock')
senses=js(A/'sens.json');routes=js(A/'couverture.json');expressions=js(A/'expressions_canoniques.json')
keys={s['key']:s for s in senses};ex={s['id']:s for s in expressions};lexids={r['id'] for r in fr}
assert len(keys)==len(senses)==226 and len(ex)==len(expressions)
norm=lambda s:' '.join(s.casefold().split())
assert len({norm(x['vaeltharyn']) for x in expressions})==len(expressions)
for s in senses:
 assert s['francais_controle'] and s['english_checked'] and s['note_fr'] and s['note_en']
 assert 'NE PAS UTILISER' not in s['note_fr']
 if not s['vaeltharyn']:continue
 assert norm(s['vaeltharyn'])==norm(ex[s['expression_id']]['vaeltharyn'])
 tokens=set(re.findall(r'[a-záéíóúý]+(?:-[a-záéíóúý]+)*',s['vaeltharyn'].lower()))
 assert tokens<=allowed,(s['key'],tokens-allowed)
 assert not re.search(r'\bTi (?:nu )?vele\b',s['vaeltharyn'])
 assert all(i in lexids for i in s['lexique_ids'])
neg=js(A/'contre_exemples.json')
assert all(s['key'] not in keys for s in neg)
raw=(A/'references/inventaire-fourni.txt').read_bytes();provenance=js(A/'references/provenance.json')
assert hashlib.sha256(raw).hexdigest()==provenance['sha256'] and len(raw)==provenance['octets']
parsed=[];language='fr'
for line,text in enumerate(raw.decode('utf-8-sig').splitlines(),1):
 if text.startswith('Anglais américain\t'):language='en';continue
 if text.startswith('Français\t'):continue
 if '\t' in text:
  cells=text.split('\t');parsed.append((line,language,cells[0].strip(),cells[1].strip()))
assert len(parsed)==len(routes)==719
assert collections.Counter(r['langue'] for r in routes)=={'fr':370,'en':349}
for row,original in zip(routes,parsed):
 assert (row['ligne'],row['langue'],row['source'],row['correspondance_fournie'])==original
 assert row['sens_cles'] and all(k in keys for k in row['sens_cles'])
 assert all(i in ex for i in row['expressions_ids'])
 assert all(row['ligne'] in keys[k]['lignes_source'] for k in row['sens_cles'])
assert [r['id'] for r in routes if not r['expressions_ids']]==['SRC-L0376','SRC-L0377','SRC-L0513','SRC-L0514']
assert keys['he_mocks']['vaeltharyn']=='Se thenthose mi.'
assert keys['causes_fear']['vaeltharyn']=='Se dityle mi, vrask.'
refs=js(A/'references/sources.json');refids={r['id'] for r in refs};assert len(refids)==12
assert all(set(r['references'])<=refids for r in routes+senses)
for filename in ['24_Inventaire_expressif_FR_EN.md','en/24_Inventaire_expressif_FR_EN.md']:
 doc=legacy_path(P,filename);t=doc.read_text(encoding='utf-8')
 for link in re.findall(r'\]\(([^)]+)\)',t):
  if link.startswith('https://'):continue
  path,_,anchor=link.partition('#');path=unquote(path)
  target=doc.parent/path if path else doc
  assert target.is_file(),(filename,link)
  if not path and anchor:assert '### '+anchor.upper().replace('S-','S-',1) in t.upper(),anchor
report={'status':'pass','source_rows':719,'sense_records':226,'new_lemmas':9,'entries':65026,'old_entries_preserved':65017,'new_canonical_expressions':200,'unestablished_source_rows':4,'validation':'written lexical, morphological, preservation, source coverage and link checks; no audio validation'}
(P/'.cache').mkdir(exist_ok=True)
(P/'.cache'/('verifier_inventaire.py.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
