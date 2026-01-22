#del keyword using objects and attributes aslo deleted using a keyword :

class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Tejas")
#delete name because this time mentioned & print in name 
# del s1.name    #-- delete object because using __ double underscore
print(s1.name)        

#del keyword using also memory and objects are indusually and both also deleted at a time :


#after delete have no effect but after delete outomatically 
del s1.name


#public and private fumction use in python 
# public = mines same ass class is attributes and objects is executed and run it the same 
# private = but private fuction only prinbt the class function not a objects function that it 

# def = private attr and methods are meant to be used only within the class and are not accesible from otside the class 

#public same in class and object 
#private function denoted by double __ 

class Person:

    def __init__(self,name):
        self.__name = name 

# p1 = Person("tejas")
# print(p1.__name)      # they are not execute because privatre fuction only execute in class not a object thats why


class Home:

    __name = "anonymous"

    def __hello(self):
        print("hello person !")

    #thats also extra function execute than after execute a private function
     
    def welcome(self):
        self.__hello()
        
h1 = Home()       

print(h1.welcome())   # there are executed because private function execute in class and print in object thata why executed 

print(h1.__hello)
