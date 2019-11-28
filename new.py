def making_array(str):
    i = 0
    letters = []
    numbers = []
    spaces = []
    punct = []
    if str == '': 
        return []
    for i, c in enumerate(str):
        if str[i].isalpha():
            if (i > 0) and (str[i-1].isalpha()):
                continue
            else:
                nomer1 = i
                pretype = alpha
        else:
            if (i > 0) and (str[i-1].isalpha()):
                data.append(str[nomer1:i])
        
        if str[i].isdigit():
            if (i > 0) and (str[i-1].isdigit()):
                continue
            else:
                nomer1 = i
                pretype = digit
        else:
            if (i > 0) and (str[i-1].isdigit()):
                numbers.append(str[nomer1:i])
        if str[i].isspace():isalpha
            if (i > 0) and (str[i-1].isspace()):
                continue
            else:
                nomer1 = i
                pretype = space
        else:
            if (i > 0) and (str[i-1].isspace()):
                spaces.append(str[nomer1:i])
        if str[i].isalpha():
            if (i > 0) and (str[i-1].isalpha()):
                continue
            else:
                nomer1 = i
        else:
            if (i > 0) and (str[i-1].isalpha()):
                data.append(str[nomer1:i])
    if str[i].isalpha():
        data.append(str[nomer1:i+1])
    return(data)
s = input
print(making_array(s))
