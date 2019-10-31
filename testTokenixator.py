import unittest
from tokenizator import Tokenizator

class making_arrayTest(unittest.TestCase):
        
    def setUp(self):
        self.Tokenizator = Tokenizator()
    def test_words_split(self):
        s = 'мама мыла раму'
        self.assertEqual(self.Tokenizator.making_array(s), [])

    def test_isalnum(self):
        s = 'а233465'
        self.assertEqual(self.Tokenizator.making_array(s), [])

    def test_isanalpha(self):
        s = 'Мамамылараму'  
        self.assertEqual(self.Tokenizator.making_array(s), ['Мамамылараму'])
        s = '7574мама 00мыла 778раму'
        self.assertEqual(self.Tokenizator.making_array(s), ['мама','мыла','раму'])
   
    def test_empty_string(self):
        s = ''
        self.assertEqual(self.Tokenizator.making_array(s), [])

if __name__== '__main__':
    unittest.main()
