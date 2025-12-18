#practice 1st question 
a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))

if(a >= b and a >= c):
    print("first is greater")
elif(b >= a and b >= c):
    print("second is greater")
else:
    print("third is greater")     


