#build in function     # user define fuction 
# print("")               #user value enter that functions is 
# print(len("hello"))     #user define function programers enter in fuction that function
# print(type(45.9))
# print(range(5))


#defult paramenters use in last not first first is no count firstly last counted
#which use in no argumenets in pass 

def mul_num(a=1, b=1): #default paramenteres 1 and also 1  than * after answer 
  print(a*b)
  return a*b

mul_num()     #no arguments

#simple question use fuction
#write a fuction the length of a list (list is a parameter)

list = [1,2,3,4,5,6,7,8,9]
def print_len(list):
  print(len(list))

print_len(list)

#write a fuction to print the element of a list in a single line (list is a paramerter) 
list = [1,2,3,4,5,6,7,8,9] #list


def print_len(list):#pareamenters
    for el in list:
       print(el,end=" ")#print in single line use end=""   
       
    
print_len(list)#argumnets    
#proper indentation mines curly braces {}  


#write a fuction find the factorial of n (n is parameter)

def cal_fact(n): #paramenter
  fact = 1
  for i in range(1,n+1):
     fact *= i
  print(fact)

cal_fact(6) #rguments
 
   
#write a fuction to convert usd to inr (usd in paramerer)
def usd_to_inr(usd):#parameter
   inr = usd *82.74
   print(inr)   
usd_to_inr(1) #arguments            #32.56

#write a fuction to check whether a number is evern or oddc(num is parameter ) #homework solved 😍
def num_to_str(num): #parameter
   if(num % 2 ==0):
      print("even")
   else:
      print("odd")
num_to_str(11) #arguments