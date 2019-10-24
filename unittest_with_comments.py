import unittest
# testing the program. for this we call the testcase class
class making_arrayTest(unittest.TestCase):
    # split breaks a string into parts using a delimiter
    # and returns these parts in a list.
    # so here we check if our program can split the string
    def test_words_split(self):
        s = 'мама мыла раму'
        self.assertEqual(s.split(), ['мама', 'мыла', 'раму'])
    # isalnum returns a nonzero value if its argument is either a letter
    # of the alphabet (upper or lower case), or a digit   
    # so here we check if our program can distinguish characters from letters
    def test_isalnum(self):
        self.assertTrue('мама23мыла34раму65'.isalnum())
        self.assertFalse('мама!помой*раму3'.isalnum())
    # isalpha returns a nonzero value if its argument is
    # a letter of the alphabet (upper or lower case). 
    # so here we check if our program can distinguish characters from letters
    def test_isanalpha(self):
        self.assertTrue('Мамамылараму'.isalpha())
        self.assertFalse('7574мама00мыла778раму'.isalpha())
if __name__== '__main__':
    unittest.main()
