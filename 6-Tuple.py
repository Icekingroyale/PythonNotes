# students = ('Alex','Chimaobi','Emmanuel','Kalu','Amadi','Amara')
# print(type(students))
# print(len(students))
# print(students)
# print(students[2])

# if 'Chimaobi' in students:
#     print('yes he is among the students')
# else:
#     print('no he is not in class')


#Editing a Tuple
#changing a character
# x = list(students)
# x[2] = 'Oge'
# students = tuple(x)
# print(students)

#adding a character
# x = list(students)
# x.append('Castro')
# students = tuple(x)
# print(x)

# x = list(students)
# del[2]
# x.remove('Emmanuel')
# # students = tuple(x)
# print(students)

#TUPLE UNPACKING      24-05-2024
students = ('Alex','Chimaobi','Emmanuel','Kalu','Amadi','Amara')
# (a,*b,c) = students
# # for i in students:
# #     print(type(i))

# print(a)
# print(b)
# print(*c)
# print(c) 
# (*c,) = students

# print(a,*b,c)

#looping through a tuple
# for i in range(len(students)):
#     print(students[i])

# x = 0
# while x < (len(students)):
#     print(students[x])
#     x += 1

#CLASS EXERCISE
# tp = (1,2,3,4,5)
# a = 0
# sum = 0
# while a < len(tp):
#     sum = sum + tp[a]
#     a += 1
# print(sum)    
    
   

