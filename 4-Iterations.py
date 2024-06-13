#16-05-2024
#ITERATION
#WHILE LOOP

# i = 0
# while i < 6:
#     print(i)
    # i += 1

# #BREAK
# i = 0
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1





# i = int(input('Enter i: '))
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print(f'{i} is not greater than 6')
    

#BREAK & CONTINUE
#BREAK terminates when condition is TRUE
# i = 0
# while i < 6:
#     i += 1
#     if i == 4:
#         break
#     print(i)


#CONTINUE skips when condition is TRUE
# i = 0
# while i < 6:
#     i += 1
#     if i == 4:
#         continue
#     print(i)


#CLASSWORK
# num = int(input('Enter the number: '))
# limit = int(input('Enter the limit: '))
# i = 1
# while i <= limit:
#     result = num * i
#     print(f'{num} x {i} = {result}')
#     # print(result)
#     i += 1




# tsum = 0
# while True:
#     num = float(input('Enter a number: '))
#     if num < 0:
#         break
#     tsum += num
# #     print(tsum)     
# print(f'Total sum = {tsum}')


    
# num = int(input('Enter the number to calculate the factorial: '))
# factorial = 1
# i = 1
# while i <= num:
#     factorial *= i
#     i += 1
# print(f'The factorial of {num}! is {factorial}')


#ASSIGNMENT
#BUILD A GUESSING GAME
# main_name = 'obie'.upper()
# guess_var = ''
# try_again = False
# trial_limit = 3
# trial_count = 0
# while guess_var != main_name and not try_again:
#     if trial_count < trial_limit:
#         guess_var = input('Enter your guess: ').upper()
#         trial_count += 1 
#     else:
#          try_again = True


# if try_again:
#     print(f' GAME OVER!!! \n your guess {guess_var} is incorrect, you have no more tries')
# else:
#     print(f' CONGRATULATIONS!!! \n your guess {guess_var} is CORRECT')
    



#FOR LOOP 17-05-2024

# students = ['Alex','Emma','Chimaobi']
# for i in students:
#     if i == 'Emma':
#         continue
#     print(i)


# for i in range(1, 11):
#     print(i)
# else:
#     print('finished')


# for i in range(1, 11, 2):
#     print(i)
# else:
#     print('finished')
    

#nested for:
# x = ['blue','red','green']
# y = ['orange','apple','banana']

# for i in x:
#     for a in y:
#         print(i,a)


#pass function
# for x in range(6):
#     pass


#CLASS WORK
# a = (input('Enter the number: '))
# factorial = 1
# i = 1
# while a <= 5:
#     factorial *= a
#     i += 1
#     print(factorial)

#ASSIGNMENT REDO THE INITIAL CLASSWORK USING FOR LOOP THIS TIME
num = int(input('Enter the number: '))
limit = int(input('Enter the limit: ')) 
i = 1
for i in limit:

    result = num * i
    print(f'{num} x {i} = {result}')
    # print(result)
    i += 1


    
num = int(input('Enter the number to calculate the factorial: '))
factorial = 1
i = 1
for i in num:
    factorial *= i
    i += 1
print(f'The factorial of {num}! is {factorial}')
