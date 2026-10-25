"""Verify canonical inputs, bilingual records, aliases, index and reference links."""
from pathlib import Path
from contextlib import closing
import hashlib,json,posixpath,re,sys,urllib.parse
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from vaeltharyn.resources import manifest
from vaeltharyn.search import connect,rows
def digest(path):
 with path.open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()
def check_links():
 files={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and not any(x in p.relative_to(ROOT).parts for x in ('.git','.cache','dist','__pycache__'))};broken=[];count=0
 for name in files:
  if not name.endswith('.md'):continue
  for raw in re.findall(r'\]\(([^)\n]+)\)',(ROOT/name).read_text(encoding='utf-8')):
   u=urllib.parse.urlsplit(raw.strip('<>'))
   if u.scheme or not u.path:continue
   target=posixpath.normpath(posixpath.join(posixpath.dirname(name),urllib.parse.unquote(u.path)));count+=1
   if target not in files and not (ROOT/target).is_dir():broken.append((name,raw))
 return count,broken
def main():
 m=manifest(ROOT);seed=json.loads((ROOT/m['provenance']['integrity']).read_text(encoding='utf-8'))
 for name,expected in seed['source_files'].items():assert digest(ROOT/name)==expected,name
 expected_data=set(seed['source_files'])|{m['provenance']['integrity'],'data/provenance/NOTICE.md'}
 actual={p.relative_to(ROOT).as_posix() for p in (ROOT/'data').rglob('*') if p.is_file()};assert actual==expected_data,(actual-expected_data,expected_data-actual)
 with closing(connect(ROOT,m)) as db:
  stored={key:json.loads(value) for key,value in db.execute("SELECT key,payload FROM records WHERE kind='entry'")}
  assert len(stored)==65045
  for lang in ('fr','en'):
   source=list(rows(ROOT/m['lexicon'][lang]['detailed']));assert len(source)==65045
   for record in source:assert stored[record['id']][lang]==record,(lang,record['id'])
  assert db.execute("SELECT count(*) FROM records WHERE kind='expression'").fetchone()[0]==456
  assert db.execute('PRAGMA quick_check').fetchone()[0]=='ok'
 count,broken=check_links()
 report={'status':'pass' if not broken else 'links_require_review','corpus_version':m['corpus_version'],'structure_version':m['structure_version'],'canonical_inputs':len(seed['source_files']),'indexed_entries_verified_field_by_field':65045,'expression_records':456,'neutral_aliases':seed['neutral_aliases'],'local_links_checked':count,'broken_links':broken}
 (ROOT/'docs/quality').mkdir(exist_ok=True);(ROOT/'docs/quality/corpus.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(report,ensure_ascii=False,indent=2))
 if broken:sys.exit(1)
if __name__=='__main__':main()
