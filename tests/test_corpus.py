"""Canonical schema, aliases, morphology and sense regressions."""
from pathlib import Path
from contextlib import closing
import csv,json,re,sys,unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from vaeltharyn.resources import manifest
from vaeltharyn.search import connect,expressions,lookup,rows,norm
class CorpusTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.m=manifest(ROOT);cls.fr=list(rows(ROOT/cls.m['lexicon']['fr']['detailed']));cls.en=list(rows(ROOT/cls.m['lexicon']['en']['detailed']))
  cls.words={r['mot']:r for r in cls.fr};cls.by_id={r['id']:r for r in cls.fr};cls.records=list(expressions(ROOT,cls.m))
  cls.aliases=json.loads((ROOT/cls.m['aliases']).read_text(encoding='utf-8'));cls.refs={r['id'] for r in json.loads((ROOT/cls.m['references']).read_text(encoding='utf-8'))}
 def test_alignment_and_status(self):
  self.assertEqual(len(self.fr),65045);self.assertEqual(len(self.en),65045);self.assertEqual(len(self.words),65042);self.assertEqual(len(self.by_id),65045)
  self.assertEqual(sum(r['categorie']=='v' for r in self.fr),6539)
  self.assertEqual([(r['id'],r['mot'],r['categorie']) for r in self.fr],[(r['id'],r['word'],r['category']) for r in self.en])
  self.assertEqual({r['statut'] for r in self.fr},{'proposition non validée','validation non documentée'})
  for row in self.fr:self.assertIn(row['source_licence'],self.refs)
 def test_expression_schemas(self):
  self.assertEqual(len(self.records),456)
  expected={'register':79,'idioms':226,'sound-body':111,'emotions-dialogue':40}
  for registry,count in expected.items():self.assertEqual(sum(raw['corpus_registry']==registry for _,raw,_ in self.records),count)
  allowed={'id','key','vaeltharyn','francais','english','francais_controle','english_checked','litteral_fr','literal_en','intensite','fonction','statut','type_equivalence','force','note_fr','note_en','references','expression_id','lexique_ids','analyses_lexicales','traitement','schema_a_completer','slots'}
  records={}
  for registry in self.m['expressions']:
   for raw in json.loads((ROOT/registry['records']).read_text(encoding='utf-8')):
    self.assertFalse(set(raw)-allowed,(registry['id'],set(raw)-allowed));key=raw.get('key',raw.get('id'));records[(registry['id'],key)]=raw
    self.assertTrue(set(raw.get('references',[]))<=self.refs)
    for identity in raw.get('lexique_ids',[]):self.assertIn(identity,self.by_id)
  self.assertEqual(len({(a['lang'],norm(a['term'])) for a in self.aliases}),len(self.aliases))
  for alias in self.aliases:
   self.assertEqual(set(alias),{'lang','term','targets','note_fr','note_en'});self.assertIn(alias['lang'],('fr','en'));self.assertTrue(alias['targets'])
   for target in alias['targets']:
    if target['registry']=='lexicon':self.assertIn(target['key'],self.by_id)
    else:self.assertIn((target['registry'],target['key']),records)
 def test_grammatical_tokens(self):
  tokens=set()
  for _,r,_ in self.records:
   text=re.sub('⟨[^⟩]+⟩','',r['vaeltharyn']);text=re.sub(r'TR-(606|808)(-(en|or|ath|ul))?','',text,flags=re.I)
   tokens.update(re.findall(r'[a-záéíóúý]+(?:-[a-záéíóúý]+)*',text.casefold()))
   self.assertNotRegex(r['vaeltharyn'],r'\bTi (?:nu )?vele\b')
  found=set()
  for row in self.fr:
   word,cat=row['mot'],row['categorie'];forms={word}
   if cat=='n':forms.update(word+s+n+c for s in ('','il','aun','va') for n in ('','i') for c in ('','en','or','ath','ul'))
   elif cat=='adj':forms.update([word+'is',word+'eth'])
   elif cat=='v':
    self.assertTrue(word.endswith('ar'));stem=word[:-2]
    forms.update(p+stem+m+e for p in ('','ra','vi') for m in ('','ir','el') for e in ('em','es','e','om','os','en'))
    forms.update(stem+s for s in ('a','ai','in','or','el'))
    forms.update(stem+'eth'+n+c for n in ('','i') for c in ('','en','or','ath','ul'))
    if row['valence'].startswith('tr'):forms.add(stem+'un')
   found.update(tokens&forms)
  found.update(p+'-'+c for p in ('mi','ti','se','min','tin','sen','si') for c in ('en','or','ath','ul'))
  missing=tokens-found
  for token in list(missing):
   parts=token.split('-')
   if len(parts)>1 and all(p in self.words and self.words[p]['categorie']=='n' for p in parts):missing.remove(token)
  self.assertFalse(missing,sorted(missing))
 def test_lookup_senses_and_aliases(self):
  cases=[('en','harmonic frequency','korthir goesumen'),('fr','faim','haem'),('vh','keth','keth')]
  for lang,term,expected in cases:
   r=lookup(ROOT,lang,[term],100)['results'][term];self.assertTrue(any(e['word']==expected for e in r['entries']) or any(e['vaeltharyn']==expected for e in r['expressions']))
  r=lookup(ROOT,'en',['exchange for mine'],100)['results']['exchange for mine'];self.assertTrue(any(e.get('schema_a_completer') for e in r['expressions']))
  r=lookup(ROOT,'fr',['Gognand'],100)['results']['Gognand'];self.assertTrue(any(not e['vaeltharyn'] for e in r['expressions']))
  r=lookup(ROOT,'vh',['Thalen moelom!'],100)['results']['Thalen moelom!'];self.assertTrue({'weird_warning','unusual'}<={e.get('key') for e in r['expressions']})
  self.assertEqual(lookup(ROOT,'en',['zoea'])['results']['zoea']['entries'][0]['word'],'soethik')
 def test_contains_and_prefix(self):
  result=lookup(ROOT,'en',['teachings'],100,mode='contains')['results']['teachings']
  self.assertTrue(any(e['word']=='taemdhyn' for e in result['entries']))
  result=lookup(ROOT,'vh',['fréquence'],100,mode='contains')['results']['fréquence']
  self.assertEqual(result['total'],0)
  result=lookup(ROOT,'en',['synthesiz'],100,mode='prefix')['results']['synthesiz']
  self.assertTrue(result['entries'] or result['expressions'])
 def test_template_and_negative_cases(self):
  templates=[r for _,r,_ in self.records if r.get('schema_a_completer')];self.assertEqual([r['key'] for r in templates],['exchange_mine']);self.assertEqual(len(re.findall('⟨[^⟩]+⟩',templates[0]['vaeltharyn'])),2)
  valid={r['vaeltharyn'] for _,r,_ in self.records}
  for case in json.loads((ROOT/'tests/fixtures/negative.json').read_text(encoding='utf-8')):
   form=case.get('forme',case.get('vaeltharyn'))
   if ' ' in form:self.assertNotIn(form,valid)
  self.assertNotIn('frekven',self.words);self.assertNotIn('kik',self.words)
  forms={word+n+c for word in ('synth','klavir','konsol','paed','transistor','kikoe','snaer','saevron') for n in ('','i') for c in ('','en','or','ath','ul')}
  self.assertEqual(len(forms),80)
if __name__=='__main__':unittest.main()
