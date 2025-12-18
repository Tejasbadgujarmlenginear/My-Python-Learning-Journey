#list is store of long variables like large data collect and inserting like :
#this type not store extra varible like but list is store sequesly store varible values
# marks = 20.2
# marks = 30.4
# marks = 60.1
# marks = 12.3
# marks = 40.3

# list it can store element different type (int,float,string,etc)j 
# java c++ not store another varible in list but python support it

marks = [20.2,30.4,60.1,12.3,40.3]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[0:5])



#string is immuble string value not be change like: indexing use but not change element not replace varibale value

str = "tejas,badgujar,badgujar,badgujar"

print(len(str))


#list is mutable this mean change the value maens chanage element varible replace the value 
student = [10,20,"Tejas","Badgujar"] #using list indexes 

print(student[2])
student[2]="badgujar"
print(student)
print(student[-4:-1])

#list slicing same as string slicing 

# same rule string name[starting_index:ending_index]  mean sublist = list part same substring= string part type 

marks = [10,30,40,50,15]
print(marks[0:4]) #ending index is not included because python not consider last index
print(marks[0:]) #outomatically detected in right all indexes because right : i written
print(marks[:5]) #same left side outoatically  included this use off python
print(marks[-5:-1])#not included last index
print(marks[-len(marks):])#this type also execute in full box 
print(marks[:])# same execute in full box 
print(marks[::-1]) #means reverse all box 
print(marks[::1])#means print full box in same order 
print(marks[::2])#means print full box in even index like 0,2,4,6,8,10 this type gap 2 after excute box
print(marks[::-2])#means print full bot in reverse like 10,8,6,4,2,0 this type after gap 2 execute box
print(marks[::-3])#means print full box even 3rd ite after like mnegative reverse like 10 7 4 1 
print(marks[::3])#same as positive after 3 rd item table print it 

#list type print table of 10 

num = list(range(1,101))  # 1 mines index 0 and step is 1 and 101 last elemnt is not counted 
table_10 = num[9::10]#print 9 is index and 10 is step so print is lisyt table in 10 
print("table 10 is :",table_10)

