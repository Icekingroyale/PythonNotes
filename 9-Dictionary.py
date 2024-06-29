car = {'brand':'benz','colour':['black','red','blue'],'model':2024,'model':1999,'sold':True}
print(car)
print(type(car))
# print(car['brand'])
# print(len(car))


# Dict constructor
# human = dict(sex = 'male',name = 'john',race = 'black',height = 6.1)
# print(human)
# print(type(human)) 

#ACCESSING A DICT
# y = human.get('height')
# print(y)

# y = human.keys()
# print(y)

# x = human.values()
# print(x)

# human['race'] = 'caucasioan'
# print(human)

#USING THE ITEMS() METHOD
# x = human.items()
# print(x)
# print(type(x))


#CHECKING IF A VALUE IS PRESENT
# if 'race' in human:
#     print('yes race is in human and the race is ' + human['race']) 

# #or
# x = human['race']
# if 'race' in human:
#     print(f'yes race is in human and the race is {x}')

#UPDATING AN ITEM IN A DICT
# human['race'] = 'asian'
# print(human)

# human.update({'race':'asian'})
# print(human)

#REMOVING AN ITEM IN A LIST
# human.pop('race')
# print(human)

# human.popitem()
# print(human)

# del human['height']
# print(human)

# human.clear()
# print(human)

# specie = human.copy()
# print(specie)


#LOOPING THROUGH A DICT
# for x in human:
#     print(human[x])

# for i in human.keys():
#     print(i)


# for i in human.values():
#     print(i)

# for x,y in human.items():
#     print(x,y)


# i = 0
# while True:
#     print(human)
#     if i == len(human):
#         break
#     i += 1


#NESTED DICTIONARY
family = { 
    'child1':{'name':'emerald','year':2019,'sex':'female'},
    'child2':{'name':'jesse','year':2022,'sex':'male'},
    'child3':{'name':'loyal','year':2024,'sex':'female'}

}
print(family['child2']['name'])

# no2 = family['child2']
# print(no2['name'])


