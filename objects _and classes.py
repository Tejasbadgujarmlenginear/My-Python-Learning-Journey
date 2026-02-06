#objects oriented programing
#class and objects in python : class are blueprint for creating objects :
#suppose every car creating after i showthing blueprint that after creating model thats type

class Home :
    name = "home_good"
    
h1 = Home()
print(h1.name)

h2 = Home()
print(h2.name)

#simple way class is blueprint and objects is realife creating the car showcasing the car 
#class mention name store values name everyinformation 
#object are mentioned car name and print there values or inforamtion 

 
class Car:    #this is class just bluprint of creating objects : first letter everytime capital
    color = "yellow"   #**mainthins is variable store the value programing name is attributes **#
    brand = "bmw"     #this like just bluprint imaging parst name driver everything stored him
    driver = "tejas"

c1 = Car()    #this is showcase off car and creating the car mentioned this car and print tere acr and car parts and values 
print(c1.color) 
print(c1.brand)
print(c1.driver)


#** init fuction is the constructor ollready assined the constructor but this time contructor in class and object assined him **#
# the self parameter is the reference to the current instance of the class and is used to access variable that belongs to the class 
class Student(): #first off clsss blueprint imagin they contructor they can using without also outomaticaly
 #assignd the contructer
 def __init__(self, fullname):  #fuction using than after init constructor are using in stored value 
    self.name = fullname    # pass the same paramenter everytime is the self nad after other parameters 
    print("adding new student in database")

s1 = Student("tejas") #they can adding new student name  
print(s1.name)  #and print name they process is the objects 
    


class Ganpati(): #assined the class name 

#defalut constructers 
   def __init__(self):
      pass
   
   #paramiterized constucters 
   def __init__(self,name,marks):  #init fuction using creating class and mentiones parameteres 1st everytime self paramenter after anothers 
      self.name =name #they can parameter assin than name and after second paramenter assining
      self.marks=marks
      print("ganesha name is adding form database") # just print extra info


g1 = Ganpati("jay ganapati",96) #executing class and values 
print(g1.name,g1.marks)       #tha n printed 

g2 = Ganpati("ganu",96)
print(g2.name,g2.marks)


#just a imagin class and object is real life applying and creating also this type also best 
class Laptop():
   name = "dell i5 eightth generation"
   quality = "good"
   features = "gaming,smooth"

lp = Laptop()
print(lp.name,lp.quality,lp.features)




#just like practice


class Ganeshji():

   def __init__(self,name,marks,age,full_name_):
      self.name =name
      self.marks =marks
      self.age =age
      self.full_name_= full_name_

g1 = Ganeshji("badgujar",99.1,"tejas badgujar",20)
print(g1.name,g1.marks,g1.age,g1.full_name_)

g2 =Ganeshji("tejas",82,20,"tejas  badgujar")
print(g2.name,g2.marks,g2.age,g2.full_name_)