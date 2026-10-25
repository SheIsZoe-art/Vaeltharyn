"""Checks the 1.5.0 supplement against its exact pre-extension Git baseline."""
from pathlib import Path
import csv,io,json,re,subprocess,hashlib,collections
P=Path(__file__).resolve().parents[1];A=P/'complements/son-corps-images-1.5.0';BASE='6d13eb624d29bb5b824cf151c900f4331cb02c67'
def read(name):
 with (P/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f,delimiter=';'))
def js(name):return json.loads((A/name).read_text(encoding='utf-8'))
fr=read('lexique_detaille.csv');en=read('en/lexique_detaille.csv')
for name in ['lexique.csv','lexique_detaille.csv','en/lexique.csv','en/lexique_detaille.csv']:
 data=read(name);oldblob=subprocess.check_output(['git','show',BASE+':'+name],cwd=P)
 old=list(csv.DictReader(io.StringIO(oldblob.decode('utf-8-sig')),delimiter=';'))
 assert len(old)==65026 and data[:65026]==old,name
 assert len(data)==65041,name
assert len({r['mot'] for r in fr})==65038
assert len({r['id'] for r in fr})==65041
assert sum(r['categorie']=='v' for r in fr)==6538
assert [(r['mot'],r['categorie'],r['id']) for r in fr]==[(r['word'],r['category'],r['id']) for r in en]
new=js('entrees_nouvelles.json');records=js('sens.json');stats=js('bilan.json')
byword={r['mot']:r for r in fr};newwords={r['fr']['mot'] for r in new}
assert len(newwords)==len(new)==15 and all(r['fr']['categorie']=='n' for r in new)
assert sum(not n['fr']['base'] for n in new)==8
assert 'frekven' not in byword and 'kik' not in byword
assert byword['korthir']['definition_fr']=='fréquence physique'
for pair in new:
 x,y=pair['fr'],pair['en'];assert x==byword[x['mot']]
 assert y==en[fr.index(x)] and x['id']==y['id']
 assert x['definition_fr']==y['definition_fr_source'] and x['api']==y['ipa']
 assert x['definition_fr'] and y['definition_en'] and x['syllabes']
 assert 'NON VALIDÉE' in x['statut'] and 'UNVALIDATED' in y['status']
 for b in x['base'].split(' + '):
  if b:assert b in byword,b

# Independent productive-form coverage, including full new noun declensions.
def forms(r):
 w,c=r['mot'],r['categorie'];yield w
 if c=='n':
  for suffix in ('','il','aun','va'):
   for number in ('','i'):
    for case in ('','en','or','ath','ul'):yield w+suffix+number+case
 elif c=='adj':
  yield w+'is';yield w+'eth'
 elif c=='v':
  st=w[:-2]
  for prefix in ('','ra','vi'):
   for mood in ('','ir','el'):
    for ending in ('em','es','e','om','os','en'):yield prefix+st+mood+ending
  for suffix in ('a','ai','in','or','el'):yield st+suffix
  if r['valence'].startswith('tr'):yield st+'un'
  for number in ('','i'):
   for case in ('','en','or','ath','ul'):yield st+'eth'+number+case
declensions={w+n+c:w for w in newwords for n in ('','i') for c in ('','en','or','ath','ul')}
assert len(declensions)==150,'Cross-collision among the fifteen new noun paradigms'
allowed=set();oldforms=set()
for r in fr[:65026]:oldforms.update(forms(r))
assert not set(declensions)&oldforms,'New lemma or noun case collides with an existing form'
for r in fr:allowed.update(forms(r))
allowed.update(p+'-'+c for p in ('mi','ti','se','min','tin','sen','si') for c in ('en','or','ath','ul'))
assert len(records)==111 and len({r['key'] for r in records})==111
lookup={r['key']:r for r in records}
for s in records:
 assert all(s[k] for k in ['source_en','vaeltharyn','francais_controle','english_checked','note_fr','note_en'])
 text=s['vaeltharyn']
 if s['schema_a_completer']:
  assert s['key']=='exchange_mine' and len(re.findall('⟨[^⟩]+⟩',text))==2
 text=re.sub('⟨[^⟩]+⟩','',text)
 text=re.sub(r'TR-(606|808)(-(en|or|ath|ul))?','',text,flags=re.I)
 for token in re.findall(r'[a-záéíóúý]+(?:-[a-záéíóúý]+)*',text.lower()):
  if token in allowed:continue
  parts=token.split('-')
  assert len(parts)>1 and all(p in byword and byword[p]['categorie']=='n' for p in parts),(s['key'],token)
 assert not re.search(r'\bTi (?:nu )?vele\b',s['vaeltharyn'])
assert lookup['only_lips']['vaeltharyn'].startswith('Ir vaemili nu velen dhoefyv, sen nu kelen')
assert lookup['harmonic_frequency']['vaeltharyn']=='korthir goesumen'
assert lookup['six_hundred_six']['vaeltharyn']=='sul khar sul transistori'
assert lookup['bloom']['vaeltharyn']=='Gegani inu naelraeren.'
assert 'pimuvath an runkusath ya min nu pipyrom' in lookup['between_laughter_certainty']['vaeltharyn']
assert 'nu rakutykom' in lookup['memory_shape']['vaeltharyn'] and 'slolnodoel' not in lookup['memory_shape']['vaeltharyn']
assert 'vethen gylgoesykath' in lookup['never_same']['vaeltharyn']
assert lookup['keyboard_hardware']['vaeltharyn']!=lookup['keyboard']['vaeltharyn']
# Sound inventory and supplied syllable onsets, excluding transparent compounds.
graphemes=re.compile(r'^(?:ae|oe|ai|ei|au|oi|th|dh|ng|[aábdeéfghiíklmnoóprstuúvyý])+$')
for n in new:
 x=n['fr'];assert graphemes.fullmatch(x['mot'].replace('-','')),x['mot']
 if not x['base']:
  syllables=x['syllabes'].split('·');assert ''.join(syllables)==x['mot']
  assert len(syllables)<=3
  assert x['mot'] in {'synth','klavir','konsol','paed','transistor','kikoe','snaer','saevron'}
  vowels={'a','á','e','é','i','í','o','ó','u','ú','y','ý','ae','oe','ai','ei','au','oi'}
  for syllable in syllables:
   parts=re.findall(r'ae|oe|ai|ei|au|oi|th|dh|ng|.',syllable)
   centers=[i for i,g in enumerate(parts) if g in vowels];assert len(centers)==1,syllable
   center=centers[0];onset=parts[:center];coda=parts[center+1:]
   assert len(onset)<=2 and len(coda)<=2,syllable
   if len(onset)==2:
    assert (onset[0] in {'b','d','dh','f','g','h','k','p','s','t','th','v'} and onset[1] in {'l','r','v'}) or (onset[0]=='s' and onset[1] in {'p','t','k','m','n','l','v'}),syllable
refs=js('references/sources.json');assert len(refs)==7 and len({r['id'] for r in refs})==7
rejected=js('contre_exemples.json');assert any(r['forme']=='frekven' for r in rejected) and any(r['forme']=='kik' for r in rejected)
assert hashlib.sha256((A/'references/source_utilisateur.txt').read_bytes()).hexdigest()==js('references/provenance.json')['source_file_sha256']
for path in [P/'25_Son_corps_et_images.md',P/'en/25_Son_corps_et_images.md']:
 for link in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
  if link.startswith('https://'):continue
  assert (path.parent/link.split('#')[0]).is_file(),link
assert not list((P/'distributions').glob('*0.3.*')),'Do not reintroduce withdrawn legacy plugin archives'
report={'status':'pass','baseline':BASE,'previous_entries_preserved':65026,'entries':65041,'new_entries':15,'new_roots':8,'new_compounds':7,'new_verb_paradigms':0,'new_noun_case_forms_checked':150,'context_records':111,'reused_physical_frequency':'korthir','semantic_duplicate_rejected':'frekven','inflection_collision_rejected':'kik','template_records':['exchange_mine'],'scope':'written lexical, phonographic and morphological checks; no audio trial; examples remain context-sensitive'}
(A/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
