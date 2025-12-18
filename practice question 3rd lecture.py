#wap to ask the user to enter name of theire 3 movies & store then in a list 

movies = []

movies.append(input("Enter 1st name : "))
movies.append(input("Enter 2nd name : "))
movies.append(input("Enter 3rd name :"))


print(movies)
              

#2nd wap to check if a list contains a palindrome of elements or not
#palindrome mines first and last same name or numbers like a :"mam","racecare" this type :
#like starting same value and last also reverse same that is palindrome

list1 = [1,2,1] #this is palindrome 
# list2 = [1,2,3] #this not palindrome 

copylist1 = list1.copy()
copylist1.reverse()
if(copylist1 == list1):
    print("palindrome")
else:
    print("not palindrome")   
    

lst = [1,2,1]
list.reverse()
if(lst ==lst[::-1]):
    print("palindrome")
else:
    print("not palindrome")    


#wap to count the number of student with "A" grade in the following 
grade = ["C","D","A","A","B","B","A"]
print(grade.count("A"))

#store a above values in a list & sort then from A to D ("A","D","A","A"," B","B","A")
#mines sorth method apply and accending order execute then like:
#and convert list it:

grade = ["C","D","A","A","B","B","A"]#accendimg order left to right sequencly printed in
grade.sort()
print(grade)