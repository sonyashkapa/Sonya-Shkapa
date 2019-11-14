""" This module contains methods and a function for tokenizing a string of characters
    
"""

def making_array(str):
    """ This function divides a string in a list of alphabetical substrings."""

    i = 0
    # set the array, in which each element will be the alphabetical chain 
    data = []  
    if str == '':
        print('строка пустая')
        return []
    # cycle that goes through each character in a string
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
    
    # set the array, in which each element will be the alphabetical chain 
        data = []  
        if str == '':
            print('строка пустая')
            return []
    # cycle that goes through each character in a string
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
def main():
    s = input()
    print(Tokenizator.tokenize(s))
    result = making_array(s)
    print(result)
if __name__== '__main__':
    main()


