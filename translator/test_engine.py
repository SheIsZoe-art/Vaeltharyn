import unittest
from .engine import noun, verb, imperative
class MorphologyTests(unittest.TestCase):
    def test_nouns(self):
        self.assertEqual(noun("sael", True, "locatif"), "saeliath")
    def test_verbs(self):
        self.assertEqual(verb("thaerar"), "thaerem")
        self.assertEqual(verb("thaerar", 5, "futur"), "vithaeren")
        self.assertEqual(verb("thaerar", 0, "passe", "conditionnel"), "rathaerelem")
    def test_imperative(self):
        self.assertEqual(imperative("thaerar"), "thaera")
if __name__ == "__main__": unittest.main()
