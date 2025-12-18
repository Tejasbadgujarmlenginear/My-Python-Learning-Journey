tup = (1, 2, 3)#error found because tuple is immutable mines
#tup[2]= 2 #not change the value this build in data type not assigning 
print(len(tup))
print(type(tup))

tup = (1,) #this is roght way to create a tuple than run it without quama use pythons assigned 
print(tup)#int float value and multiple value quama is optinal without quama run it 
print(type(tup))

#indexing also in i tuple like  

tup = (20, 30, 40)
print(tup[1])
print(tup[:])
print(tup[:2])#lats index not counted but first is counted 
print(tup[0:])

#slicing also use in tuple

tup = (2,1,4,5,6,7)

print(tup[0:2])#lasty index not counted right 
print(tup[0:])#assigned the parentheses thaa left side everyone than run it 
print(tup[:5])#so last index not counted right but starting index counted 
print(tup[-1])#negative indexing start in -1 and right side last in
print(tup[-5:-1])#last negative index alos not counted  strted -1 so not run 7

#tuple methods :

tup = (2,2,3,3,4,2,5)
#direct found it what element in first index in first occurence mines index finds :
print(tup.index(5))#--(element find index)
#same as count method in tuple:
#this element what time repeate this so fimnd it count method 
print(tup.count(2))#--(element find index how time repeates in tuple)
