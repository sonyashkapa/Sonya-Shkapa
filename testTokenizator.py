import unittest
import tokenizator
from tokenizator import Tokenizator

class MakingArrayTest(unittest.TestCase):
        
    def setUp(self):
        self.Tokenizator = Tokenizator()
        
    """ "split" breaks a string into parts using a delimiter
    and returns these parts in a list.
    so here we check if our program can split the string"""

    def test_words_split(self):
        s = 'мама мыла раму'
        self.assertEqual(self.Tokenizator.making_array(s), ['мама','мыла','раму'])
        
    """ "isalnum" returns a nonzero value if its argument is either a letter
     of the alphabet (upper or lower case), or a digit   
     so here we check if our program can distinguish characters from letters"""

    def test_isalnum(self):
        s = 'а233465'
        self.assertEqual(self.Tokenizator.making_array(s), ['а'])
        
    """ "isalpha" returns a nonzero value if its argument is
     a letter of the alphabet (upper or lower case). 
     so here we check if our program can distinguish characters from letters"""

    def test_isanalpha(self):
        s = 'Мамамылараму'  
        self.assertEqual(self.Tokenizator.making_array(s), ['Мамамылараму'])
        s = '7574мама 00мыла 778раму'
        self.assertEqual(self.Tokenizator.making_array(s), ['мама','мыла','раму'])
        
    """ program check if an empty string is entered"""
    def test_empty_string(self):
        s = ''
        self.assertEqual(self.Tokenizator.making_array(s), [])
    
class TestUnittest(unittest.TestCase):

""" "isalnum" returns a nonzero value if its argument is either a letter
 of the alphabet (upper or lower case), or a digit
 so here we check if our program can distinguish characters from letters"""

    def test_isalnum(self):
        self.assertTrue('мама23мыла34раму65'.isalnum())
        self.assertFalse('мама!помой*'.isalnum())
        
""" "isalpha" returns a nonzero value if its argument is
 a letter of the alphabet (upper or lower case).
 so here we check if our program can distinguish characters from letters"""

    def test_isanalpha(self):
        self.assertTrue('Мамамылараму'.isalpha())
        self.assertFalse('7574мама00мыла778раму'.isalpha())
        
     """ program check if an empty string is entered"""    

    def test_empty_string(self):
        s = ''
        self.assertEqual(tokenization.making_array(s), [])
        
# do not forget to insert this module into the code you are checking
if __name__== '__main__':
unittest.main()


