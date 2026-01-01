# 1 store following world meaning in a python dictionary 
# table : "a piece of furniture", list of facts and fighures
# cat : "a smalll animal"

#so first off all logic like dictionalry store values and two values store like 
#tupple form and list form also posible so these like :

dictionary = {
    "cat" : "a small animal",
    "table"  : ["a piece of furniture","list of facts and figures"]
    #both values are store also list and tuple format also possible because values
    #added all types also possible
    
}
print(dictionary)

# 2 you are given a list off subjects for students assume 1 classroom required for 1 
# subject how many classroom needed by all students  :


subjects = {
    "python","java","c++","python","java",
    "c","javascript","html","css","c++"
}
print(subjects.union)
print("total classroom needed :",len(subjects))

# 3 wap to enter marks of 3 subjects from the user and store then in a dictionary start with an empty 
#dictionary and add one by one use subject name as key and marks as value

#logic input 3 subjects 1st enter 1st 2nd 3rd subjects marks and store empty dictionary one by one so use update methode 
# because update method add one by by dictionary format so use like 
marks = {}

a = input("enter 1st subject marks :")
marks.update({"math":a})

b = input("enter 2nd subject marks :")
marks.update({"science":b})

c = input("enter 3rd subject marks :")
marks.update({"it":c})

print("student marks ",marks)

# 4 figure out way to store 9 & 9.0 as seprete values in the set (you can help in build in data types)
# because set is mutable but key are immutable so and value are mtable so these thing also possible like :

values = {
   ("float",9.0),
   ("int",9),
}
print(values)
