import math
a = float(input("Введите частоту подкорпуса:"))
b = float(input("Введите частоту других текстов:"))
c = float(input("Введите объем подкорпуса:"))
d = float(input("Введите объем других текстов:"))
e1 = c * ((a+b)/(c+d))
e2 = d * ((a+b)/(c+d))
print("E1 = ",e1,", E2 = ",e2)
g = a/e1
g2 = b/e2
g_in_sqr = 2 * (a* math.log1p(g) + b*math.log1p(g2))
f_terms = (a+1)/(b+1)                                                
print("Log-likelyhood = ",g_in_sqr)
print("f terms = ",f_terms)                                                
                                                
