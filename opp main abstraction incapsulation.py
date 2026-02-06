#abstaction : 

#hinding impleamentation detail only main feature anr showing in user:


class Car():

    def __init__(self):
        self.brack = False
        self.cluchh = False     #these type mines unusage details are hiding only showing main feature thats 
        self.acc = False        #thats like opnly show car stared like cluchh brack they not showing this type abstraction

    def Start(self):
        self.breck = True
        self.cluchh = True
        self.acc = True
        print("Car started.....")

car1 = Car()
car1.Start()       


#incapsulation

#wrapping data and objects into single unit and objects
#mines use class objects attributes and fuction that execute single objects that its a incapsulation
#same after code class and objects code ucing attribute fuction and calss and objects

