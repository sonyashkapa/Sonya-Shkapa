
import unittest
import gener
from gener import Tokenizator
from gener import Token


class TestTokenizatorOfCategories(unittest.TestCase):  

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
        self.t = Tokenizator()

    def test_words_split(self):
        s = 'мама мыла раму'
        self.assertEqual(self.t.tokenize(s), ['мама','мыла','раму'])

    def test_isalnum(self):
        s = 'а233465'
        self.assertEqual(self.t.tokenize(s), ['а'])

    def test_isanalpha(self):
        s = 'Мамамылараму'  
        self.assertEqual(self.t.tokenize(s), ['Мамамылараму'])
        s = '7574мама 00мыла 778раму'
        self.assertEqual(self.t.tokenize(s), ['мама','мыла','раму'])

    def test_empty_string(self):
        s = ''
        self.assertEqual(self.t.tokenize(s), [])

class TestUnittest(unittest.TestCase):
 
    def test_isalnum(self):
        s = 'мама23мыла34раму65'
        self.assertEqual(gener.making_array(s), ['мама','мыла','раму'])
        s = 'мама!помой*'
        self.assertEqual(gener.making_array(s), ['мама','помой'])

    def test_isanalpha(self):
        s = 'Мамамылараму'
        self.assertEqual(gener.making_array(s), ['Мамамылараму'])
        s ='7574мама00мыла778раму'
        self.assertEqual(gener.making_array(s), ['мама','мыла','раму'])

    def test_empty_string(self):
        s = ''
        self.assertEqual(gener.making_array(s), [])
        
class GeneratorTest(unittest.TestCase):
        
    def test_alpha(self):
        gen = list(Tokenizator.gen_tokenize_cat('1мама мыла рому'))
        self.assertEqual(gen[1].token, 'мама')
        self.assertEqual(gen[1].category, 'alpha')
        
    def test_space(self):
        gen = list(Tokenizator.gen_tokenize_cat('мамамыларому'))
        self.assertEqual(gen[0].token, 'мамамыларому')
        
    def test_digit(self):
        gen = list(Tokenizator.gen_tokenize_cat('012345'))
        self.assertEqual(gen[0].token,'012345')
        self.assertEqual(gen[0].category,'digit')
        self.assertEqual(gen[0].firstindex, 0)
        self.assertEqual(gen[0].lastindex, 6)
        
    def test_nonapha(self):
        gen = list(Tokenizator.gen_tokenize_cat('мама123мыла'))
        self.assertEqual(gen[1].token,'123')
        self.assertEqual(gen[1].category,'digit')
        
if __name__ == '__main__':
    unittest.main()
