import unittest
import translator as tl

class TestTranslator(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(tl.french_to_english(None), '')
        self.assertEqual(tl.french_to_english(''), '')
        self.assertEqual(tl.french_to_english('Hello'), 'Hello')
        self.assertEqual(tl.french_to_english('Bonjour'), 'Hello')

    def test_englishToFrench(self):
        self.assertEqual(tl.english_to_french(None), '')
        self.assertEqual(tl.english_to_french(''), '')
        self.assertEqual(tl.english_to_french('Bonjour'), 'Bonjour')
        self.assertEqual(tl.english_to_french('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()
