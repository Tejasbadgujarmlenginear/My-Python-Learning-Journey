# 1 set is mutable 
# 2 set elements is immutable
# 2 set is unordered because every element every position get not fix 
# 3 set is hasheble value mines one time value fix so fix than is immutable 
# 4 Set is mutable → unhashable.
# 5 Set elements (keys inside) must be immutable → hashable

num = {1,2,3,4,"string","welcome",True,12.2} 

print(num)

#empty set print like 

num = {} #these like empty dictionary not set
print(type(num))

#so usually assigned the set like 

num = set() #manually assigned the value because curley braces same {} in dic set so :
print(type(num)) #and these like empty set ;syntax


#sets methods :
#add method use in add element in sets
collection = set()
collection.add(1)
collection.add(2)
collection.add(2) #so these not printed because is repeate and set key is immutble so these not printed 
collection.add("name")#these also possible because is string is immutable so posible
collection.add((1,2,3))#these also possible because tuple also immutable so possible 
#collection.add([1,2])#these not possible because they have list is mutable value 
#and sets keys is immutable so these everytime change value in list dic so not print some error found
#like unhashable error mines hashing value not same like
#[1,2],[1,2] so this hashing value these is immutable but same way [1,2],[1,2,3] so these a unhashable value because a mutable these error found
print(collection)

#remove method use in remove the element and value the sets like :

collection = {1,2,3,4,"name",True}
collection.remove(2)
print(collection)

#clear method use in set like :

collection = {"Tejas","Badgujar",} # use in set empty than use the clear method 
collection.clear()
print(len(collection)) #because clear the all set its use the clear method

#pop method use in removes random values like :

collection = {"Tejas","Badgujar","Learning","Coding"}
print(collection.pop())

#union methods use in combine both sets and circulate value like repeat they have printed only one time like :

collection1 = {1,2,3} #because 2 & 3 is repeated so 2 & 3 is single time consider
collection2 = {2,3,4} #output {1,2,3,4,} because this repeated but sinle time consider 
print(collection1.union(collection2)) # also reverse use 1 & 2 collection but same answer because combine values consider single 

#intersection methods use in sets is repeated value consider and they printed 

collection1 = {1,2,3} #2 & 3 is repeated in combine both sets and repeted value is printed not print another values like 
collection2 = {2,3,4} #{2,3} because is repeated so only this printed not another values printed 
print(collection1.intersection(collection2))