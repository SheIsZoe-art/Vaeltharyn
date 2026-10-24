import unittest
from .translate import translate_assisted
class FakeLex:
    va_col="vaeltharyn"; fr_col="français"
    def lookup(self, token, direction):
        if token.lower() in ("chante","thaerem"):return [{"vaeltharyn":"thaerem","français":"chante"}]
        return []
    def analyze(self, token):return []
class TranslateTests(unittest.TestCase):
    def test_known(self):
        self.assertEqual(translate_assisted(FakeLex(),"Je chante.")["output"],"mi thaerem.")
    def test_unknown_is_visible(self):
        self.assertIn("⟦mystère⟧",translate_assisted(FakeLex(),"mystère")["output"])
if __name__=="__main__":unittest.main()
