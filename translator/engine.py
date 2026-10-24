"""Moteur lexical et morphologique Vaeltharyn, sans dépendance externe."""
import csv
import re
import unicodedata
from pathlib import Path

PERSONS = ("em", "es", "e", "om", "os", "en")
PRONOUNS = ("mi", "ti", "se", "min", "tin", "sen")
CASES = {"direct": "", "genitif": "en", "datif": "or", "locatif": "ath", "instrumental": "ul"}
TENSES = {"present": "", "passe": "ra", "futur": "vi"}
MOODS = {"indicatif": "", "subjonctif": "ir", "conditionnel": "el"}

def norm(s):
    return unicodedata.normalize("NFC", s).casefold().strip()

def noun(lemma, plural=False, case="direct"):
    if case not in CASES: raise ValueError("Cas inconnu")
    return lemma + ("i" if plural else "") + CASES[case]

def verb(infinitive, person=0, tense="present", mood="indicatif"):
    if not infinitive.endswith("ar"): raise ValueError("Infinitif attendu en -ar")
    if person not in range(6): raise ValueError("Personne 0..5")
    return TENSES[tense] + infinitive[:-2] + MOODS[mood] + PERSONS[person]

def imperative(infinitive, plural=False):
    if not infinitive.endswith("ar"): raise ValueError("Infinitif attendu en -ar")
    return infinitive[:-2] + ("ai" if plural else "a")

class Lexicon:
    def __init__(self, csv_path):
        self.entries = []
        self.fr = {}
        self.va = {}
        with open(csv_path, encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f, delimiter=";")
            self.columns = reader.fieldnames or []
            for row in reader:
                self.entries.append(row)
        self.va_col = next((c for c in self.columns if "vael" in norm(c)), self.columns[0] if self.columns else None)
        self.fr_col = next((c for c in self.columns if "fran" in norm(c)), self.columns[1] if len(self.columns)>1 else None)
        if not self.va_col or not self.fr_col: raise ValueError("Colonnes lexicales non détectées")
        for row in self.entries:
            self.va.setdefault(norm(row[self.va_col]), []).append(row)
            for key in re.split(r"[,;/]", row[self.fr_col]):
                if norm(key): self.fr.setdefault(norm(key), []).append(row)

    def lookup(self, word, direction="fr-va"):
        return self.fr.get(norm(word), []) if direction == "fr-va" else self.va.get(norm(word), [])

    def analyze(self, word):
        key = norm(word)
        hits = [{"lemma": row[self.va_col], "analysis": "lemme", "entry": row} for row in self.va.get(key, [])]
        for suffix, case in ((s, c) for c, s in CASES.items() if s):
            if key.endswith(suffix):
                stem = key[:-len(suffix)]
                for plural in (False, True):
                    lemma = stem[:-1] if plural and stem.endswith("i") else stem
                    for row in self.va.get(lemma, []):
                        hits.append({"lemma": lemma, "analysis": f"nom {case} {'pluriel' if plural else 'singulier'} (hypothèse)", "entry": row})
        for tense, prefix in TENSES.items():
            if prefix and not key.startswith(prefix): continue
            stem = key[len(prefix):]
            for mood, marker in MOODS.items():
                for i, ending in enumerate(PERSONS):
                    tail = marker + ending
                    if stem.endswith(tail) and len(stem)>len(tail):
                        lemma = stem[:-len(tail)] + "ar"
                        for row in self.va.get(lemma, []):
                            hits.append({"lemma": lemma, "analysis": f"verbe {tense} {mood} {PRONOUNS[i]} (hypothèse)", "entry": row})
        return hits

    def gloss(self, text, direction="fr-va"):
        parts = re.findall(r"\w+(?:['’-]\w+)*|[^\w]+", text, re.UNICODE)
        return [{"token": p, "candidates": self.lookup(p, direction)} for p in parts if p.strip()]

def open_default():
    return Lexicon(Path(__file__).resolve().parents[1] / "lexique.csv")
