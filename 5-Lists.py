#SEQUENCE IN PYTHON  20-05-2024

#LISTS
# scores = [20,30,50.0,90,30,35,'man',False]
# print(scores)
# print(len(scores))
# print(type(scores))

#creating a lsit using a "LIST CONSTRUCTOR", ""=list(())""
scores = list((20,30,50.7,90,30,35,'man',True))
print(scores)
print(len(scores)) #calling the length of characters in the list
print(type(scores)) #calling the datatype

#calling the index
# print(scores[3])  
# print(scores[3:7])
# print(scores[3])
# print(scores[3:])
# print(scores[:3])
# print(scores[-3]) 
# print(scores[-3:-1]) 


# if 30 in scores:
#     print('yes we have it')
# else:
#     print('not available')




# a = input('Enter character: ')
# if a in scores:
#     print('yes we have it')
# else:
#     print('not available')

#using BREAK & CONTINUE inside your list
# lists = [20,30,50.7,90,30,35,"man",True]


# for x in lists:
#     if x == "man":
#         break
#     print(x)

# for x in lists:
#     if x == 30:
#         continue
#     print(x)

#Changing an element in your list
# lists[3] = 'obie'
# lists[3:5] = ['obie',False,420] 
# print(lists)


#editing a list
# students = ['Alex','John','Obi','Ada','Kalu','Obi', 'AMANDA', 'OBIANUJU', 'Amanda']

# students.extend (scores)
# students.append('okoro')
# students.insert(2,'Amadi')
# students.remove('Alex')
# students.pop(3)
# students.pop()
# del students[3]
# del students
# students.clear()
# students.sort()
# students.sort(key= str.lower)
# # x = set(students)
# print(x)
# print(type(x))
# print(set(students))
# print(students)


#ASSIGNMENTS

# fruits = ['banana','mango','orange','pawpaw','watermelon','apple']
# fruits.reverse()
# print(fruits)


# numbers = [34,60,20,30,50.0,90,30,35,20,17,45,]
# numbers.sort()
# # numbers.sort(reverse=True)
# print(numbers)


# remove_repeated = set(numbers)
# print(remove_repeated)


# a = max(numbers)
# print(a)


# b = min(numbers)
# print(b)


# numbers.sort(reverse = True)
# print(numbers[1])


# del numbers[4]
# print(numbers)


# numbers.insert(0,4)
# print(numbers)


# common = list(set(numbers) & set(scores))
# print(common)



#23-05-2024
#LIST COMPREHENSION
fruits = ['banana','orange','mango','BANANA','apple','cherry']
x = [i for i in fruits if 'a' in i]

# foods = ['fufu','spaghetti','rice','beans','garri']
# newlist=(foods + fruits)
# print(newlist)


# for i in foods:
#     fruits.append(i)
# print(fruits)