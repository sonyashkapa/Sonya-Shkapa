"""It is docstring of the module, which provide tokenization functions
"""
class Tokenizator(object):
    def making_array(str):
    """ This function gets a string on input,
    and it gives an array of
    alphabetical chains as output 
    """
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
if __name__== '__main__':
    making_array = Tokenizator()
    s = input()
    print(Tokenizator.making_array(s))


