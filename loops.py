#loops are used in repeat instructions 
count = 1 #iterators this is mines one variable repeat and loop theniterators and loop ander repeat instruction that is iteration 
while count <=10:
    print("hello",count)
    count +=1

print(count)    



i = 1
while i<=5:
    print(i)
    i+=1
#this is print of 5 numbers 

#print as reverse numbers 

i = 5
while i <= 6:
    print(i)
    i+=1

print("loop ended")    

#questions of while lopp simple wat like :

# 1 queprint number from 1 to 100      #12:48 lecture start

i = 1 #this is iterater 
while i<=100: #and using while loop 
    print(i)
    i+=1

# 2 que print number from 100 to 1 

i = 100
while i>=1:
    print(i)
    i-=1


# 3 que print the multiplication table in the n number 

n = 3

while n <= 30: #these also good but they have my logic also diffrent like :
    print(n)
    n+=3

#these also good means ever umber print also possible 
n = int(input("enter the number :"))
i = 1
while i<=10:
    print(n*i)
    i+=1     

# 4 que print the list using loop 

nums = [1,4,9,16,25,36,49,64,81,100]

print(nums[:]) #using indexing possible but they ask only loop using than print list 



nums = [1,4,9,16,25,36,49,64,81,100]
#traverse like :
idx = 0
while idx < len(nums):
    print(nums[idx])

    idx += 1

# 5 que find the number in this tuple 
nums = (1,4,9,16,25,36,49,64,81,100)

x = 36
i = 0
while i< len(nums):
   
    if(nums[i] == x):
        print("index found",i)  
    else:
        print("finding....")    
    i+=1
 