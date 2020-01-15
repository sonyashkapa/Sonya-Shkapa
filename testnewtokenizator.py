import unittest
import newtokenizer
from newtokenizer import Tokenizator
from newtokenizer import Token


class TestTokenizatorWithCategories(unittest.TestCase):  

    def setUp(self):
        self.t = Tokenizator()

    def test_alpha(self):
        s =self.t.tokenize_cat('1мама мыла рому')
        self.assertEqual(s[1].token, 'мама')
        self.assertEqual(s[1].category, 'alpha')
       
    def test_space(self):
        s = self.t.tokenize_cat('мамамыларому')
        self.assertEqual(s[0].token, 'мамамыларому')
        
    def test_digit(self):
        s = self.t.tokenize_cat('012345')
        self.assertEqual(s[0].token,'012345')
        self.assertEqual(s[0].category,'digit')
        self.assertEqual(s[0].firstindex, 0)
        self.assertEqual(s[0].lastindex, 6)
        
    def test_nonapha(self):
        s = self.t.tokenize_cat('мама123мыла')
        self.assertEqual(s[1].token,'123')
        self.assertEqual(s[1].category,'digit')


class MakingArrayTest(unittest.TestCase):
 
    def setUp(self):
        self.T = Tokenizator()

    def test_words_split(self):
        s = 'мама мыла раму'
        self.assertEqual(self.T.tokenize(s), ['мама','мыла','раму'])

    def test_isalnum(self):
        s = 'а233465'
        self.assertEqual(self.T.tokenize(s), ['а'])

    def test_isanalpha(self):
        s = 'Мамамылараму'  
        self.assertEqual(self.T.tokenize(s), ['Мамамылараму'])
        s = '7574мама 00мыла 778раму'
        self.assertEqual(self.T.tokenize(s), ['мама','мыла','раму'])

    def test_empty_string(self):
        s = ''
        self.assertEqual(self.T.tokenize(s), [])

class TestUnittest(unittest.TestCase):
 
    def test_isalnum(self):
        s = 'мама23мыла34раму65'
        self.assertEqual(newtokenizer.making_array(s), ['мама','мыла','раму'])
        s = 'мама!помой*'
        self.assertEqual(newtokenizer.making_array(s), ['мама','помой'])

    def test_isanalpha(self):
        s = 'Мамамылараму'
        self.assertEqual(newtokenizer.making_array(s), ['Мамамылараму'])
        s ='7574мама00мыла778раму'
        self.assertEqual(newtokenizer.making_array(s), ['мама','мыла','раму'])

    def test_empty_string(self):
        s = ''
        self.assertEqual(newtokenizer.making_array(s), [])
        

if __name__ == '__main__':
    unittest.main()
