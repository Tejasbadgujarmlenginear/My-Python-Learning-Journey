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

#outomatically assinged the percentage becaue @properties function using 

stu1 = Student(98,100,99,99) 
print(stu1.percentage)      

stu1.che = 98
print(stu1.percentage)
