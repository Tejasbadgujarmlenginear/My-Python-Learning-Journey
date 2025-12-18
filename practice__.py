num = list(range(1,971))
table_100 = num[96::97]#96 is index and 97 is step so print is list table in 97
print("table 100 is :",table_100)

#simple way to print everytype table of n value :
# start → kahan se start karna hai

# stop → kahan tak numbers chahiye (stop excluded)

# step → kitne gap ke baad next number lena hai


n = int(input("enter the number to print table :")) 
table = list(range(n, n*12, n))  # start=n, stop=n*11, step=n
print(table)

#using list tuple possible only strng not possible because string is character print table of n value like :