#CLASS & OBJECTS       07-06-2024

# class my_class:
#     x = 5
# print(my_class)

#__init__ class
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# obj = person("Chimaobi",27)
# print(obj.name,obj.age)


#OBJECT METHOD
# class person:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#     def my_func(self):
#         print('Hello my name is ' + self.name)

# greet = person('chimaobi',1997)
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