#Wap to check if a number entered by the user is odd or even 
num = int(input("enter number : "))

if(num % 2 == 0 ):
    print("even")
else:
    print("odd")    


#wap to find the gretest of 4 numbers entered by the user 

a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))
d = int(input("enter fourth number :"))

if(a >= b and a >= c and a >= d):
    print("First number is largest",a)
elif(b >= a and b >= c and b >= d):
    print("second number is largest",b) 
elif(c >= a and c >= b and c >= d):
    print("third is larest number ",c)
else:
    print("fourth is larest number ",d)


#wap to check if a number is a multiply of 7 or not 

a = int(input("enter a number :"))

if(a % 7 == 0):
    print("Multiply of 7 ")
else:
    print("not multiply of 7 ")    
