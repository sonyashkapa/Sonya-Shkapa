""" This module contains methods and a function for tokenizing a string of characters
    
"""

import unicodedata
def making_array(str):
    """ This function divides a string in a list of alphabetical substrings."""

    i = 0
    # set the array, in which each element will be the alphabetical chain 
    data = []  
    if str == '': 
        return []
    # loop that goes through each character in a string
    for i, c in enumerate(str):
        # checking if the character is an alphabetical char
        if str[i].isalpha():
            # if the character is an alphabetical char
            # then we check it's index and the previous element 
            if (i > 0) and (str[i-1].isalpha()):
                continue
            else:
                #  we remember the index of the first char in the alphabetical chain
                nomer1 = i
        else:
            # if the character is not char, we check it's index and the previous character
            if (i > 0) and (str[i-1].isalpha()):
                # if it's the last char in the alphabetical chain
                # then we add this chain to the array
                data.append(str[nomer1:i])
    # checking the last character in our string, whether it is letter or not 
    # if the last character was alphabetic
    # then the cycle does not meet non-alphabetic one to save the last alphabetic chain  
    if str[i].isalpha():
        data.append(str[nomer1:i+1])
    return(data)

class Tokenizator(object):
    
    """ This class uses the method to divide a string in a list of alphabetical substrings."""

    def tokenize(self,str):
        
        """ This method divides a string in the array of alphabetical substrings."""
        i = 0
        data = []
        if str == '':
          return []
        # loop that goes through each character in a string
        for i, c in enumerate(str):
            # checking if the character is an alphabetical char
            if str[i].isalpha():
                # if the character is an alphabetical char
                # then we check it's index and the previous element 
                if (i > 0) and (str[i-1].isalpha()):
                    continue
                else:
                    #  we remember the index of the first char in the alphabetical chain 
                    nomer1 = i
            else:
                # if the character is not char, we check it's index and the previous character 
                if (i > 0) and (str[i-1].isalpha()):
                    # if it's the last char in the alphabetical chain
                    # then we add this chain to the array
                    data.append(str[nomer1:i])
        # checking the last character in our string, whether it is letter or not 
        # if the last character was alphabetic
        # then the cycle does not meet non-alphabetic one to save the last alphabetic chain
        if str[i].isalpha():
            data.append(str[nomer1:i+1])
        return(data)
    @staticmethod 
    def defcategory(char):
         
         """ This method is used for determining 4 categories """
         
         if char.isalpha():
            category = 'alpha'
         elif char.isdigit():
             category = 'digit'
         elif char.isspace():
            category = 'space'
         elif unicodedata.category(char)[0] == 'P':
            category = 'punct'
         else:
            category = 'unknown'
         return category
    
    def tokenize_cat(self, str):
        """
        This method adds token, its category, 
        index of first and last char of substring in initial string 
        
        """
        data2 = []
        if len(str) == 0:
            return []
        else:
            # loop that goes through each character in a string
            for i, c in enumerate(str):
                category = Tokenizator.defcategory(c)
                if i == 0:
                    index = i
                    prevcat = category
                # check if we didn't reach the last character of the string
                else:
                     if (i+1) < len(str):
                         # we compare categories of current and next characters
                         # if they differ, so we have reached the last characters of the category 
                         if category != prevcat:
                             token = str[index:i]
                             t = Token(token, prevcat, index, i)
                             data2.append(t)
                             index = i
                             prevcat = category
            # check the last character in the string
            token = str[index:]
            i = i + 1  
            t = Token(token, category, index, i) 
            data2.append(t)         
        return data2
    
class Token(object):
    """
    Class representing information about the token
    Token type,first and last indexes in original string
    """     
    def __init__(self, t, categ, frstind, lstind):      
         self.firstindex = frstind
         self.lastindex = lstind
         self.token = t
         self.category = categ

    def __repr__(self):
          
        """ Method of building printable outcome """
        
        return ' ' + self.token + ' is  ' + self.category + ' located from ' + str(self.firstindex) + ' index to ' + str(self.lastindex) + ' index.' + '\n'
    
def main():
    t = Tokenizator()
    str = 'мама 2!'
    print(t.tokenize_cat(str))

if __name__ == '__main__':
    main()
