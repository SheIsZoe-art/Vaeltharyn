"""Sense, morphology and lookup constraints for emotion and dialogue."""
from pathlib import Path
import json,sys,unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from vaeltharyn.search import lookup,rows,norm

class EmotionDialogueTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.lex=list(rows(ROOT/'data/lexicon/fr/entries.csv'));cls.words={r['mot']:r for r in cls.lex}
  cls.records=json.loads((ROOT/'data/expressions/emotions-dialogue/sens.json').read_text(encoding='utf-8'))
 def test_no_duplicate_constructions(self):
  forms=[norm(r['vaeltharyn']) for r in self.records];self.assertEqual(len(forms),40);self.assertEqual(len(set(forms)),40)
  m=json.loads((ROOT/'corpus.json').read_text(encoding='utf-8'))
  old={norm(r['vaeltharyn']) for reg in m['expressions'] if reg['id']!='emotions-dialogue' for r in json.loads((ROOT/reg['records']).read_text(encoding='utf-8'))}
  self.assertFalse(old&set(forms))
 def test_bilingual_record_lookup(self):
  for lang,field in [('fr','francais_controle'),('en','english_checked')]:
   terms=[r[field] for r in self.records]
   results=lookup(ROOT,lang,terms,100)['results']
   for r in self.records:
    self.assertIn(r['key'],{e.get('key') for e in results[r[field]]['expressions']},(lang,r['key']))
 def test_formations_and_collisions(self):
  compounds={'thim-raelun','thaem-nael','saelraev-dathak'}
  new=compounds|{'trukoemar'}
  self.assertEqual(self.words['trukoemar']['base'],'trukoem');self.assertEqual(self.words['trukoemar']['valence'],'intr')
  for word in compounds:
   self.assertTrue(all(self.words[p]['categorie']=='n' for p in word.split('-')))
  finite={'trukoem'+m+e for m in ('','ir','el') for e in ('em','es','e','om','os','en')}
  candidates={p+v for p in ('','ra','vi') for v in finite}
  candidates|={w+s+n+c for w in compounds for s in ('','il','aun','va') for n in ('','i') for c in ('','en','or','ath','ul')}
  collisions=set()
  for r in self.lex:
   w,cat=r['mot'],r['categorie']
   if w in new:continue
   forms={w}
   if cat=='n':forms.update(w+s+n+c for s in ('','il','aun','va') for n in ('','i') for c in ('','en','or','ath','ul'))
   elif cat=='v':
    stem=w[:-2];forms.update(p+stem+m+e for p in ('','ra','vi') for m in ('','ir','el') for e in ('em','es','e','om','os','en'))
    forms.update(stem+s for s in ('a','ai','in','or','el','eth'))
    if r['valence'].startswith('tr'):forms.add(stem+'un')
   elif cat=='adj':forms.update([w+'eth',w+'is'])
   collisions.update(candidates&forms)
  # Regular noun + ar derivation shares its 3PL with the base noun's genitive.
  self.assertEqual(collisions,{'trukoemen'})
  self.assertEqual('trukoem'+'en','trukoemar'[:-2]+'en')
  self.assertIn('trukoemen',self.words['trukoemar']['note'])
 def test_lexical_aliases_preserve_sense(self):
  cases=[('fr','désir','vael'),('fr','volonté','vael'),('fr','cœur','naevan'),('fr','coeur','naevan'),('fr','silence','thaemnyr'),('en','will','vael'),('en','heart','naevan'),('en','silence','thaemnyr'),('en','can','kelar')]
  for lang,term,word in cases:
   with self.subTest(lang=lang,term=term):
    result=lookup(ROOT,lang,[term],100)['results'][term]
    entry=next(e for e in result['entries'] if e['word']==word)
    self.assertTrue(entry.get('alias_matches'));self.assertTrue(all(a['note_fr'] and a['note_en'] for a in entry['alias_matches']))
  self.assertEqual(self.words['roenythar']['definition_fr'],'Ne pas partir, en parlant du coup d\'une arme à feu, lorsqu’on veut tirer.')
  self.assertEqual(self.words['sloekoem']['definition_fr'],'Saveur de ce qui est amer.')
 def test_contextual_paraphrases_and_actors(self):
  for lang,term,key in [('fr','tu me manques','absence_felt'),('en','I miss you','absence_felt'),('fr','joie douce-amère','bittersweet_joy'),('en','bittersweet joy','bittersweet_joy')]:
   result=lookup(ROOT,lang,[term],100)['results'][term]
   expression=next(e for e in result['expressions'] if e.get('key')==key)
   self.assertTrue(expression['note_fr'] and expression['note_en'])
   self.assertEqual(expression['force'],0)
  r={v['key']:v for v in self.records}
  self.assertEqual(r['want_be_heard']['vaeltharyn'],'Mi vaelem dhe ti lises mi.')
  self.assertEqual(r['desire_not_consent']['vaeltharyn'],'Mi dhavem vael, ath mi nu vaerem thaevlyren.')
  self.assertEqual(r['chosen_company']['vaeltharyn'],'Mi vaelem momlaevar ko ti.')
  self.assertIn('continua',next(v for v in self.records if v['key']=='still_love_leave')['note_fr'])
  self.assertTrue(all(not e['schema_a_completer'] for e in self.records))

if __name__=='__main__':unittest.main()
