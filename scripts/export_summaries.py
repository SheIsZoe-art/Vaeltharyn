"""Generate optional lightweight CSV views without storing duplicate source datasets."""
from pathlib import Path
import csv,json
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/'corpus.json').read_text(encoding='utf-8'))
for lang,fields in [('fr',['mot','categorie','domaine','sens','valence']),('en',['word','category','domain','meaning','valency','id'])]:
    target=ROOT/'dist/exports'/lang/'summary.csv';target.parent.mkdir(parents=True,exist_ok=True)
    with (ROOT/m['lexicon'][lang]['detailed']).open(encoding='utf-8-sig',newline='') as source,target.open('w',encoding='utf-8',newline='') as output:
        writer=csv.DictWriter(output,fieldnames=fields,delimiter=';',lineterminator='\n');writer.writeheader()
        for row in csv.DictReader(source,delimiter=';'):writer.writerow({k:row[k] for k in fields})
    print(target)
