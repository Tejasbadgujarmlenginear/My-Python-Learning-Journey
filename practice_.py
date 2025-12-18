

a =  float(input("enter first marks of a is :"))
b =  float(input("enter second marks of b is :"))
c =  float(input("enter third marks of c is :"))
d =  float(input("enter fourth marks of d is :"))


if(a>=b and a>=c and a>=d):
    print("i am a and my marks and grade is highest")
    grade = "A 😍"
elif(b>=a and b>=c and b>=d):
    print("i am b and my marks and grade is highest")
    grade = "B 😍"
elif(c>=a and c>=b and c>=d):
    print("i am c and my marks and grade is highest")
    grade = "C 😍"
elif(d>=a and d>=b and d>=c ):
    print("i am d and my marks and grade is highest")
    grade = "D 😍"

print("my grade is :",grade)