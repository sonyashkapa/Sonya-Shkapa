def making_array(str):
    i = 0
    letters = []
    numbers = []
    spaces = 0
    punct = []
    if str == '': 
        return []
    for i, c in enumerate(str):
        if str[i].isalpha():
            if (i > 0) and (str[i-1].isalpha()):
                continue
            else:
                nomer1 = i
        else:
            if str[i].isspace():
                spaces = spaces+1
            else:
                if str[i].isdigit():
                    numbers.append(str[i])
                else:
                    punct.append(str[i])
        
            if (i > 0) and (str[i-1].isalpha()):
                letters.append(str[nomer1:i])
    if str[i].isalpha():
        letters.append(str[nomer1:i+1])
    return(letters)
s = input
print(making_array(s))
