# #10/05/2024
#OPERATORS
#ARITHEMETIC OPERATORS

a = 30 #int
pie = 3.142 #float
c = 20.62j #complex
print(type(a))
print(type(pie))
print(type(c))




x = 7
y = '2' #TypeError because you cant concatenate (add +) a string with an integer
result = x + y
print(result) 


# #USE OF MODULUS
x = int(input('Enter the number:'))
if x % 2 == 0:
    print(f'the number {x} is an even number')
    print(x,'the number is an even number')
    print('the number ' + str(x) + ' is an even number')
else:
    print(f'the number {x} is an odd number')
    print(x,'the number is an odd number')
    print('the number ' + str(x) + ' is an odd number')


#FLOAT DIVISION / INTEGER DIVISION
x = 7
y = 2
result = x // y
print(result)


#ASSIGNMENT OPERATORS
x = 5
y = 2
x = y
print(x)

x = 7

x += 3
x = x + 3

x -= 3
x = x - 3

x *= 3
x = x * 3

print(x)

#LOGIC OPERATORS
x = 5
print(x > 5 and x < 10)

#MEMBERSHIP & iDENTITY OPERATORS
x = 'hello world'
print('hello' not in x)
y = 'hello world'
print(x in y)
print(x is y)
print(x is not y)


#BOOL
print(type(True))
print(type(False))
print(1 == 1)
print(1 != 1)
print(bool(20))
print(bool(-20.5)) #non trivial values are converted to true
print(bool(0))
print(bool('string'))
print(bool('')) #trivial values are converted to false

#Python sees 1 as True & 0 as False
print(5 + True) # 5 + 1 = 6
print(10 * False) # 10 * 0 = 0  