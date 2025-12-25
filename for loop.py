#for loop for use in sequenciall traversal for traversing list,string,tuple etc.


# list = [1,2,3,4,7,5,8,]
# for num in list:
#     print(num)

tup = (10,20,30,40,50)    
for num in tup:
    print(num)

#search for a number x in this tuple using loop

num = (1,2,4,6,8,9,12,45,67,45) #index vise search this mean (linear search)
x = 45

idx = 0
for el in num:
    if(el == x):
        print("num found at index",idx)
        break
    idx+=1


#for loop also using range function 
#same indexing but range type start form 0 and negative start form -1 
#steps start:end:step 
#only 1 to 10 print last not print 
for el in range(11): #only (start) condition execute 
    print(el)

#only 2 to 10 element count last not count 
for el in range(2,11): #both (start:stop) condition execute 
    print(el)

#only 1 t0 10 number printed last index not counted 
for el in range(1,11,1): #both (start:stop) condition execute 
    print(el)

#only 100 to 1 reverse number printed last index not counted 
for el in range(100,0,-1): #both (start:stop) condition execute 
    print(el)

#every table printed 
n = int(input("enter number"))

for el in range(n,n*11,n): #both (start:stop:step) every tale count condition execute 
    print(el)        
                       
n = int(input("enter number"))

list_table = list(range(n, n*11, n))
print(list_table)











