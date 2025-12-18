#dictonary methods : 
student = {
    "name" : "tejas Badgujar", #name & subjects is keys so print only keys not nesting keys 
    "subjects" : { #nesting in dictionary 
        "math" : 91,
        "it" : 96,
    }
}    
print(len(student))
print(list(student))

#keys method method use in count total keys in dictionary 
print(student.keys())

#values method use in keys value print and also nesting values also included like 

print(student.values()) #these is dict but convert also list like :
print(list(student.values()))

#items method return keys, val pair as tuple
print(student.items()) #also convert in list 
print(list(student.items())) 

#and also possible sepreate keys like :

pairs = list(student.items())
print(pairs[1])

#dic get method uses in print key like 
print(student.get("name")) #methods use because is after lot off program that run 
#but this is rong then print none and other like :

print(student["name"]) #these also same output but sometime incorrect value 
#than after lot off code errrr because use simple :

print("hellow welcome my coding learning")


#update method use in dictonary new keys added in old dic use in {} curley braces like :

student.update({"interest" : "ai","age" : 20})
print(student)

#and also dublicate keys update like suppose :

student.update({"name" : "Tejas badgujar",})  #thess is not values in copy keys but update methode after added new keys
print(student)

