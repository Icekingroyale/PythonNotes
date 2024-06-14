# name = input('Enter your name: ').upper()
# while name != 'AMADI':
#          print(f'Mr. {name} who you??')
# print('My guy!!')


# name = ''
# while True:
#        name =  input('Enter your name: ').upper()
#        if name != 'ICEKING':
#                 print(f'Mr. {name} who you??')
#        else:
#             print(f'{name} my guy! \nWelcome!!!')
#             break


# BUILD A GUESSING GAME
# main_name = 'obie'.upper()
# guess_var = ''
# try_again = True
# trial_limit = 3
# trial_count = 0
# while trial_count != trial_limit and try_again:
#     if trial_count < trial_limit:
#         guess_var = input('Enter your guess: ')
#         trial_count += 1
#     else:
#         not try_again

# if try_again:
#     print(f' GAME OVER!!! \n your guess {guess_var} is incorrect, you have no more tries')
# else:
#     print(f' CONGRATULATIONS!!! \n your guess {guess_var} is CORRECT')


# name = input('Enter your name: ').upper()
# print(name.upper())
# a = name.upper()
# print(a)
# a = name.split()
# a = name.len()
# print(len(a))


# num = (1,2,3,4,5,6)
# sum = 0
# # i = 0
# # while i <= len(num):
# #     sum = sum + i
# #     i += 1
# # print(sum)


# for n in num:
#     sum = sum + n
# print(sum)


# def greet(name,age):
#     print(f"Happy birthday {name}, \nYou are {age} years old today")

# # greet('iceking',27)


# def vikings(*warriors):
#     print(f"The best fighter is {warriors[3]}")

# vikings('lagather','rollo','bjorn','ragner','king harald','ivar the boneless')
# # vikings('ali','fraser','lewis','tyson','foreman','holyfield')




# def area(l, w):
#     print(l * w)


# area(4, 5)


# def is_even(num):
#     if num % 2 == 0:
#         print(True)
#     else:
#         print(False)

# is_even(5) 
# is_even(6)
# is_even(2.0)   


# def test():
#     print( 2+4 )
#     return

# test()



# def string_int(txt):
# 	a = input("Enter a string number: ")
# 	print(int(a))
# 	return a
# string_int(5)

# print(type(string_int(5)))


class student():
    def __init__(self,name,regno,dept,sex):
        self.name = name
        self.regno = regno
        self.dept = dept
        self.sex = sex

obj = student('obie',103,'csc','male')
print(obj.name + ' ' + obj.dept)