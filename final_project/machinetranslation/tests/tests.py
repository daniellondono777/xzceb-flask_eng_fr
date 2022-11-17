import unittest

from translator import english_to_french, french_to_english

class TranslateE2FTest(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french("Hello"), "asfsa") 
        self.assertEqual(english_to_french("Yes"), "Oui") 
        self.assertEqual(english_to_french("Hello"), "Bonjour" )
        self.assertEqual(english_to_french(" "), " ") 

class TranslateF2ETest(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english("Bonjour"), "sdgd") 
        self.assertEqual(french_to_english("Bonjour"), "Hello") 
        self.assertEqual(french_to_english("Maison"), "House") 
        self.assertEqual(french_to_english(" "), " ") 

unittest.main()
