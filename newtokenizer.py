import unicodedata
def making_array(str):
    i = 0
    data = []  
    if str == '': 
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

class Tokenizator(object):

    def tokenize(self,str):
        i = 0
        data = []
        if str == '':
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
    def catdef(self, char):       
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
    def tokenize_categories(self, str):
        data2 = []
        if len(str) == 0:
            return []
        else:
            for i, c in enumerate(str):
                category = self.catdef(c)
                if i == 0:
                    index = i
                    prevcat = category
                elif (i+1) < len(str):
                    if category != prevcat:
                        token = str[index:i]
                        t = Token(token, prevcat, index, i)
                        data2.append(t)
                        index = i
                        prevcat = category
            token = str[index:]
            i = i + 1  
            t = Token(token, category, index, i) 
            data2.append(t)         
        return data2
    
class Token(object):

    def __init__(self, t, cat, fi, li):
      
        self.token = t
        self.category = cat
        self.firstindex = fi
        self.lastindex = li

    def __repr__(self):
        return ' ' + self.token + ' is  ' + self.category + ' located from ' + str(self.firstindex) + ' index to ' + str(self.lastindex) + ' index.' + '\n'
    
def main():
    t = Tokenizator()
    str = 'мама 2!'
    print(t.tokenize_categories(str))

if __name__ == '__main__':
    main()
    
