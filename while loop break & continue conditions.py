
#break condition  is mainlly use for stop the loop after not execute in program 
nums = (1,4,9,16,25,36,49,64,81,100)

x = 36
i = 0
while i< len(nums):
   
    if(nums[i] == x):
        print("index found",i)  
        break #breack condition use in stop the loop after value not executed 
        
    else:
        print("finding....")    
    i+=1
 
#continue use in loop like    


i = 1
while i <=10:
    if(i%2 != 0):
     i+=1
     continue #continue condition mainlly use for skip the number 
    print(i)
    i+=1                             