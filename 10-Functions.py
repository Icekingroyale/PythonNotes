# FUNCTIONS    06-06-2024

# def hello():
#     global x
#     x = 5
#     y = 7
#     result = x + y
#     print(result)
# hello()

# def SI(p,r,t):
#     i = (p*r*t)/100
#     print(i)
# SI(500,5,10)


#Args &  Par
# def SI(p,r,t):
#     i = (p*r*t)/100
#     print(i)
# p = int(input('enter your principal: '))
# r = int(input('enter your rate: '))
# t = int(input('enter your time: '))
# SI(p,r,t)


#Arbitrary Args (*Args)
def children(*kids):
    print(f'The second child is {kids[1]}')
children('okeke','okafor','okonkwo','okorie')

#KEYWORD ARGS




#DEFAULT PAR VALUE



#RETURN STATEMENT
# def calculate(x):
#     return 5 * x
# print(calculate(3))


#RECURSIVE FUNCTION
# def tri_recursion(k):
#     if (x>0):
#         result = k + tri_recursion(k-1)
#         print(result)
#     else:
#         result = 0
#     return result
# tri_recursion