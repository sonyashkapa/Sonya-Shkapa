class Tokenizator(object):
    def making_array(str):
        i = 0
        data = []
        if str == '':
            print('строка пустая')
            return []
        for i, c in enumerate(str):
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
if __name__== '__main__':
    making_array = Tokenizator()
    s = input()
    print(tokenizator.making_array(s))