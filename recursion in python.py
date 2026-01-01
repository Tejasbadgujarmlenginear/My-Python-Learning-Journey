#recursion when a fuction calls itself repetedly is called recursion

#example of recursion

def show(n):
    if(n == 0): # : base case 
        return
    print(n)
    show(n-1)

show(5)        


# factorial of n using recursion

def fact(n): 
    if(n ==0 or n ==1): #base case
     return 1
    return n*fact(n-1)
print(fact(5))

#practice question 
#write a function to calculate the sum of first n natural number using recursion

def sum_n(n):
   if(n == 0): #base case
      return 0
   return sum_n(n-1) + n

print(sum_n(5))


#write a recursive fuction to print all elements in a list
#hint : use list & index as a parameter

def print_list(list,index=0):
   if(index == len(list)): #base case
      return
   print(list[index])
   print_list(list,index+1)

num = [10,20,30,40,50]

print_list(num)
