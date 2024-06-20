#CLASS & OBJECTS       07-06-2024

# class my_class:
#     x = 5
# print(my_class)

#Exercise1 on OOP
#A class that displays students that pass or failed

#create the class
class student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks       

#input args to match the number of pars in the class
# std1 = student('chimaobi',100) 
# std2 = student('henry',92)
# std3 = student('somto',68)
# std4 = student('onyebuchi',38)
# std5 = student('chisom',24)

# #create a list obj to hold this parameters
# obj = [std1,std2,std3,std4,std5]

# #iterate through this list to print pass and failed students
# for i in obj:
#     if i.marks >= 50:
#         print(f'{i.name} passed with a score of {i.marks}')
#     elif i.marks < 50:
#         print(f'{i.name} failed with a score of {i.marks}')


        
#Exercise12 on OOP


        

#__init__ class

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# obj = person("Chimaobi",27)
# obj2 = person('Henry',28)
# print(obj.name,obj.age)
# print(obj2.age,obj2.name)


#OBJECT METHOD
# class person:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#     def my_func(self):
#         print(f'Hello my name is {self.name}')

#     def my_func2(self):
#         print(f'I {self.name}, am going to make history')

# greet = person('chimaobi',1997)
# greet2 = person('henry',1996)
# greet.my_func()




# INHERITANCE
# class cars:
#     def __init__(self, car, model):
#         self.car = car
#         self.model = model

#     def my_car(self):
#         print(self.car,self.model)

# class ugbo(cars):
#     pass

# x = cars('toyota','lexus')
# x.my_car()


# class cars:
#     def __init__(self, car, model):
#         self.car = car
#         self.model = model

#     def my_car(self):
#         print(self.car,self.model)

# class ugbo(cars):
#     def __init__(self,car,model):
#         # cars.car + cars.model
#         cars.__init__(self,car,model)

# x = cars('toyota','lexus')
# x.my_car()