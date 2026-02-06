#practice question 
# : create student class that takes names and marsk in 3 subjects as argument in constructor then create a method to print the average

class Students():

    def __init__(self,name,marks,branch):
        self.name = name
        self.marks = marks
        self.branch = branch

    def get_average(self):

        sum = 0
        for val in self.marks:
            sum += val

        print("hi",self.name,"your total average is :",sum/3)




s1 = Students("Tejas",[67,76,96],"bca")
# print(s1.name,s1.marks,s1.branch)

s1.get_average()


#practice suppose you branch print 