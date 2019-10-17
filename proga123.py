"""It is docstring of the module."""
def massiv(str):
    """ Function gets a string on input,
    and it gives an array of
    alphabetical chains as an output """
    # set the array
    data = []  
    # cycle that goes through each element in a string
    for i,c in enumerate(str):
        # checking if the element is a letter
        if str[i].isalpha():
            # if the element is a letter, then we check it's index and the previous element 
            if (i>0) and (str[i-1].isalpha()):
                continue
            else:
                #  we remember the index of the first letter in an alphabetical chain 
                nomer1 = i
        else:
            # if the element is not a letter, we check it's index and the previous element 
            if (i>0) and (str[i-1].isalpha()):
                # if it's the last letter in the alphabetical chain, then we add this chain to the array
                data.append(str[nomer1:i])
    # checking the last element in a string, whether it is a letter or not 
    if str[i].isalpha():
        data.append(str[nomer1:i+1])
    return(data)
# enter the line
s = input()
print(massiv(s))


