# mainly three methods are showing in class 
# @staticmethod  these they not acces or change in other method like cals
# classmethod  this pass (cls) arguments pass
# @instamcemethod  so this pass (self) arguments pass

# class method :  usuaqlly use in 

# usually assinged hime cls 

class Student():

    name = "tejas"

    # def fullname(self,name):
    #     self.name=name

    
    @classmethod
    def changeName (cls,name):
        cls.name=name

s1 = Student() 
s1.changeName("tejas")
print(s1.name)       
print(Student.name)



# @properties
# usually use in some times print marks but change marks some time but as a possiblke but retry new values 
# they are irriteted so thats why @properties are use like :

class Student():

    def __init__(self,math,phy,che,bio):
        self.math=math
        self.phy=phy
        self.che=che
        self.bio=bio
    
    def calculatepercentage(self):
        self.percentage = str((self.math + self.phy + self.che + self.bio) / 4)  + "%"

stu1 = Student(98,100,99,99) 
stu1.calculatepercentage() 
print(stu1.percentage)      

stu1 = Student(98,100,99,99) 
stu1.calculatepercentage() 
print(stu1.percentage)      

stu1.phy = 80     #this goog because you chage value but not possible to direct 
print(stu1.phy)   #change in percentage that why use in @properties

print(stu1.percentage) #why no changing because direct change not possible

#thats why using @properties 

class Student():

    def __init__(self,math,phy,che,bio):
        self.math=math
        self.phy=phy
        self.che=che
        self.bio=bio
    
    # def calculatepercentage(self):
    #     self.percentage = str((self.math + self.phy + self.che + self.bio) / 4)  + "%"


    @property
    def percentage(self):
        return  str((self.math + self.phy + self.che + self.bio) / 4)  + "%"

#outomatically assinged the percentage because @properties function using 

stu1 = Student(98,100,99,99) 
print(stu1.percentage)      

stu1.che = 98
print(stu1.percentage)


#polymorphism 
# poly =many terms 
# so usually operater use in many form thats it polymorphism 
# usually suppose complex number are adding so use dunder fuction that assing _ _ 
# complex mines like 1i+4j 2i+5k = that is not possible in class obeject so thats use in dunder function 


class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2): #these thing use render funtion than after execute simple way in add complex number 
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    

    def __sub__(self,num2): 
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)


num1 = Complex(1 ,3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()                         # also use sum mult like just assing him like 
 
num3 = num1 + num2
num3.showNumber()

num3 = num1-num2
num3.showNumber()


# q.1 practice quetion 
#define a circle class to create a circle with radius r using the constructor. 
# define an area() method of the class which calculate the area of the cicle.
# define a parameter() method of the class which alloow you calculate the parimeter of the circle 

class Circle():
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def parimeter(self):
        return 2 * (22/7) * self.radius



c1 = Circle(21)

print(c1.area())
print(c1.parimeter())

#q.2 practice question
# define a employee class with attributes role deparment & salary. this class also showdetails()method.ModuleNotFoundErro
# create an engineer class that inherits properties from employees &

class Employee():
   def __init__(self,role,dept,salary):
       self.role = role
       self.dept = dept 
       self.salary = salary
   
   def showDetail(self):
       print("role =",self.role)
       print("dept =",self.dept)
       print("salary =",self.salary)
    
    
class Engineer(Employee):
   def __init__(self,name,age):
       self.name =name
       self.age =age
       super().__init__("software Engineer","Tech",20000000)
          

# e1 = Employee("engineer","tech",100000)
# e1.showDetail() 

engg1 = Engineer("tejas Badgujar","21")
print(engg1.name,engg1.age)
engg1.showDetail()


#q.3 practice question
#create a class called order which stores item & its price.
# use dunder fuction __get__() to convey that:
# order1>order2 if price of order1>price order2

class Orders():
    def __init__(self,items,price):
        self.items =items
        self.price =price

    def __gt__(self,odr2):
        return self.price > odr2.price    

odr1 = Orders("watch",299)
odr2 = Orders("sunglass",290)
print(odr1>odr2)   #tru output because that the gretest is first       