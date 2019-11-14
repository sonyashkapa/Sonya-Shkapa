import unittest
import tokenizator
from tokenizator import Tokenizator

class MakingArrayTest(unittest.TestCase):
 
    def setUp(self):
        self.tokentest= Tokenizator()

    def test_words_split(self):
        s = 'мама мыла раму'
        self.assertEqual(self.tokentest.tokenize(s), ['мама','мыла','раму'])
 
    def test_isalnum(self):
        s = 'а233465'
        self.assertEqual(self.tokentest.tokenize(s), ['а'])
                
    def test_isanalpha(self):
        s = 'Мамамылараму'  
        self.assertEqual(self.tokentest.tokenize(s), ['Мамамылараму'])
        s = '7574мама 00мыла 778раму'
        self.assertEqual(self.tokentest.tokenize(s), ['мама','мыла','раму'])
        
    def test_empty_string(self):
        s = ''
        self.assertEqual(self.tokentest.tokenize(s), [])

class TestUnittest(unittest.TestCase):

    def test_isalnum(self):
            s = 'мама23мыла34раму65'
            self.assertEqual(tokenizator.making_array(s), ['мама','мыла','раму'])
            s = 'мама!помой*'
            self.assertEqual(tokenizator.making_array(s), ['мама','помой'])

      def test_isanalpha(self):
            s = 'Мамамылараму'
            self.assertEqual(tokenizator.making_array(s), ['мамамылараму'])
            s ='7574мама00мыла778раму'
            self.assertEqual(tokenizator.making_array(s), ['мама','мыла','раму'])

      def test_empty_string(self):
            s = ''
            self.assertEqual(tokenizator.making_array(s), [])
       

if __name__== '__main__':
    unittest.main()


