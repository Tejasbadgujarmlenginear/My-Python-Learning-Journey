#11 : 07  
#inheritance :like pass out emotions values thats its mines
#1st genrateion class to move in 2nd generation tat is inheritance 
#example parents thoughts get passing the children they child 
#derived like inherite mines receive the knowledge everything

#1st car logic everything included so after some days later 2nd car executed in code so logic 
#same only car name are diffrent so thats time only derived the information inherit the car information
#thats it inheritance
# like base and parent mines giving 
#like child and derived mines recieve the information
# #simple


# class Car:
#     #inforations suppose


# class ToyotaCar(Car):    #parantesis and bracket mentioned in derived the car inherit the class    


class Car:
    color = "yellow"
    @staticmethod
    def start():  
        print("Car Started")
                                              #one bass class 
    @staticmethod
    def stop():
        print("Car Stopped") 

class ToyotaCar(Car): #inherits the 2nd toyota car in 1st carjust assinged the class car_name(car):
    def __init__(self,name):
        self.name=name
                                            #one derived class mines 
car1 = ToyotaCar("lamborgini")              #single level inheritance
car2 = ToyotaCar("fortuner")
  
print(car1.color)
print(car1.name)
print(car1.start())


#type of inheritance minly 3 type 
#single inheritance  :one base and one derived class same upper example like one parent class and one child class 
#multilevel inheritance
#multiple inheritance


#multilevel inheritance 

class Car:

    @staticmethod
    def start(): 
        print("car started...")       #1st class mentioned base class 

    @staticmethod
    def stop():
        print("car stoped...")


class ToyotaCar(Car):
    def __init__(self,brand):   #2nd class derived class derived the information and they also base in 3rd class 
        self.brand = brand

class fortuner(Car):
    def __init__(self,type):  # 3rd class they is derived class mines they have child class derived the information
         self.type = type


car1 = fortuner("diesel")
car1.start()                    #that process its a mutiple inheritance bothes off classes base and derived multiple that can multi_level ineritance



#multiple inheritance 
#simple like multiple base clases and just one derived class recieving the information they can possible 
#like suppose example :
#two base classes information gain in one derived class and create also own class in derived thats is a multple ineritance 
#simple example    
class A:
    varA = "welcome to the A class"
class B:                            #two or more than base clases 
    varB = "Welcome to the B class"

class C(A, B):                       #and one derived class mines child class 
    varC ="Welcome to the C class"

c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)



#super()  method mainly use some time executed class bluprint but not mentioned in objects but mentioned him derived calss so
#thats smae thing avilavble in derived class so access in super method that possible like 

class Car:

    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():  
        print("Car Started")
                                              
    @staticmethod
    def stop():
        print("Car Stopped") 

class ToyotaCar(Car): #
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)  #they derived class assined the type but not assinged in base class so base class also executed thats the super metopd using possible
        super().start()          #this start manually also and derived class super method use in they also possible
                                            
car1 = ToyotaCar("prius","electric")

print(car1.type)

# car1.start()    this a car start in class they everytime but some time lot off data so thats time not mentioned him object 
#executed so and derived class same objects or item avilable so redirect and execute iin the that use in super method 