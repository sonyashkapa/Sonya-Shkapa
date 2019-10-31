import unittest
from tokenizator import Tokenizator

class making_arrayTest(unittest.TestCase):
        
    def setUp(self):
        self.Tokenizator = Tokenizator()
    def test_words_split(self):
        s = 'мама мыла раму'
        self.assertEqual(self.Tokenizator.making_array(s), [])

    def test_isalnum(self):
        s = 'мама23мыла34раму65'
        self.assertEqual(self.Tokenizator.making_array(s), [])
        s = 'мама!помой*раму3'
        self.assertEqual(self.Tokenizator.making_array(s), [])

    def test_isanalpha(self):
        s = 'Мамамылараму'  
        self.assertEqual(self.Tokenizator.making_array(s), [])
        s = '7574мама00мыла778раму'
        self.assertEqual(self.Tokenizator.making_array(s), [])
   
    def test_empty_string(self):
        s = ''
        self.assertEqual(self.Tokenizator.making_array(s), [])

if __name__== '__main__':
    unittest.main()
