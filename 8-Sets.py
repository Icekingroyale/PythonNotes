# #SETS   31-05-2024

students = {'alex','chimaobi','emma','Ebere','chimaobi'}
# students2 = {'okeke','amanda','onyeka'}
# students3 = ['henry','sikito']

# # sets = {True,2,3,4,5,1}
# # print(len(sets))
# # print(len(students))
# # print(type(students))

score = set((90,75,65,33,71,80))
print(type(score))

for i in students:
    print(i)

# # print('emma' in students)

# # students.add('emerald')
# # print(students)

# student_all = students.union(students2)
# # print(student_all)
# # student_all = students|students2
# print(student_all)

# students2.update(students3) 
# print(type(students2))

# students2.remove('nweke') #items does not exist so we have an Error!
# print(students2)

# students2.discard('nweke')  #item does exist yet no Error!
# print(students2)

# students.pop(2)
# print(students)

# students.clear()
# print(students)

#JOINTIN SETS 
# set2 = students.union(students,students3,student_all,score)
# print(set2)
# set2 = student_all|students|score
# print(set2)

# #INTERSECTION
# set1 = {2,4,6,9,5}
# set2 = {6,3,7,5,4,8}

# set3 = set1.intersection(set2)
# print(set3)
# print(set1.intersection(set2))
# set3 = (set1 & set2)
# print(set3)

# #DIFFERENCE
# set4 = set1.difference(set2)
# print(set4)
# set4 = set1 - set2
# print(set4)

# set5 = set1.symmetric_difference(set2)
# print(set5)
# set5 = set1 ^ set2
# print(set5)
 
# set6 = set1.symmetric_difference_update(set2)
# set1.symmetric_difference_update(set2)
# print(set1)
# print(set6)