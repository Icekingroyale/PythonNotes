#REGULAR EXPRESSION        20/06/2024

import re
txt = 'the rain in Spain'
# a = re.search('^the.*spain',txt)
# if a:
#     print('yes')
# else:
#     print('no')

# b = re.findall('ain',txt)
# print(b)

# c = re.search('\s',txt)
# print('the white space character is/are',c.start())

# d = re.split('\s',txt)
# e = re.split('\s',txt,1)
# print(d)
# print(e)

# f = re.sub('\s','_',txt) #replaces white space with chosen characters
# g = re.sub('\s','_',txt,2) #controls the number of places to replace
# print(f)
# print(g)

# h = re.search(r"\bS\w+",txt)
# print(h)
# print(h.group())

# i = re.findall('\Athe',txt)
# print(i)

# j = re.findall(r'\bain',txt) #searches for raw string 'ain' in the beginning of a text
# k = re.findall(r'ain\b',txt) #searches for raw string 'ain' at the end of a text
# print(j)
# print(k)

# l = re.findall(r'\Bain',txt) #checks if the raw string 'ain' is not at the end of a text
# m = re.findall(r'ain\B',txt) #checks if the raw string 'ain' is not at the beginning of a text
# print(l)
# print(m)

# n = re.findall('\d',txt)
# print(n)

# o = re.findall('\D',txt)
# print(o)

#Set of Expressions
# p = re.findall('[arn]',txt)
# print(p)

# q = re.findall('[a-n]',txt)
# print(q)

# r = re.findall('[^arn]',txt)
# print(r)

# s = re.findall('[0123]',txt)
# print(s)

# t = re.findall('[0-9]',txt)
# print(t)

# txt2 = '8 times before 11:45 AM'
# u = re.findall('[0-5][0-9]',txt2)
# print(u)

