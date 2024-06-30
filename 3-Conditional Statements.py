#13/05/2024
#CONDITIONAL STATEMENTS

age = int(input('how old are you: '))
if age >= 18:
    print("you're eligible to vote")
else:
    print("you're not eligible to vote")


num_1 = int(input('enter first number: '))
numm_2 = int(input('enter the second number: '))
if num_1 > numm_2:
    print(str(num_1) + (' is higher' ))
elif numm_2 > num_1:
    print(str(numm_2) + ' is higher')
else:
    print('both are equal')


age = int(input('how old are you: '))
if age <= 0:
    print('invalid data')
elif age <= 12:
    print('you are not a teenager')
elif age <= 19:
    print('you are a teenager')
elif age <= 40:
    print('you are an adult')
elif age > 40:
    print('you are a grandpa')
else:
    print('invalid data')


#CLASS WORK
#N0: 1

score = int(input('what is your score: '))
if score >= 70:
    print('your grade is A')
elif score <= 69:
    print('Your grade is B')
elif score <= 59:
    print('Your grade is C')
elif score <= 49:
    print('Your grade is E')
elif score < 40:
    print('Your grade is F')



#N0: 2
num_1 = int(input('enter first number: '))
numm_2 = int(input('enter the second number: '))
if num_1 > numm_2:
    print('numa_ 1 is higher' )
else:
    print('num_2 is higher')



#NO: 3
year = input('Enter  the Year: ')
year1= int(year)
if len (year)== 4:

    if (year1 % 4 == 0 and year1 % 100 != 0) or (year1 % 400 == 0):
        print(f'This year {year1}: is a leap year')
    else:
        print(f'This year {year1}: is NOT a leap year')
else:
    print(f'The year {year1}: is not a valid year')

#NO: 4
#BASIC CALCULATOR
 
a = int(input('Enter first number: '))
x = input("Enter operator: ")
b = int(input('Enter second number: ' ))

if x == '+': 
    print(a + b)
elif x == '-':
    print(a - b)
elif x == '*':
    print(a * b)
elif x == '/':
    print(a / b)



#ASSIGNMENT 14-05-2024
#NO: 1

x = input('Enter Some Characters: ')
a = x.split
print(a)


#NO: 2
a = int(input('Enter a number: '))
if a > 1 and a % 2 == 1:
    print('PRIME')
else:
    print('NOT PRIME')


#NO 3:
a = int(input('Enter your Principal: '))
b = int(input('Enter your interest rate %: '))
c = int(input('Enter time in years: '))
si = (a * b * c)/100
print(f'Simple Interst = {si}')