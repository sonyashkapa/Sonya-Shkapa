def massiv(str):
    data = []
    for i,c in enumerate(str):
        if str[i].isalpha():
            if (i>0) and (str[i-1].isalpha()):
                continue
            else:
                nomer1 = i
        else:
            if (i>0) and (str[i-1].isalpha()):
                data.append(str[nomer1:i])
    return(data)
s = input()+' '
print(massiv(s))


