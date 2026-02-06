#programer sine is every time open also but close everytime in file that is secure
#you not close your files is changeble thats it.
# variable store value in first is file name and second is mode means you are right read or then thats it .

#only add file 
f = open("file save data.py","a")
f.close()


#than only read the file
f = open("file save data.py","r") #open file & read
data = f.read() # data and read file 
print(data) #print then
print(type(data)) #type of these like string or files 
f.close() # close the file 

#specing indexing element also possible in file thats like :

f = open("file save data.py","r") #open file & read
data = f.read(5) #file specific indexes posible to access the element character
print(data) #print then
print(type(data)) #type of these like string or files 
f.close() # close the file 

#they can possible also in one line read at a time at a time 

f = open("file save data.py","r") #open file & read
line1 = f.readline() #file specific indexes posible to access the element character
print(line1) #print then
print(type(line1)) #type of these like string or files 
f.close() # close the file 

#1 st time read file that 2nd time print file lines they have only empty spaces not
#repeat the value because you olready reaf thise file and everysingle line you read then 
# a spece everytime include because every programer next line than code write up they use \n that a spece include 

#write and add the data 

f = open("file save data.py","w") #mode w means wirte the data

f.write("\nand they have store in data is writed")

f.close()

# add the data in file 

f = open("file save data.py","a") #mode a means add the data 

f.write("\nthats is add the data")

f.close()

#theys have suppose without write add only just you file and mode name write and add they also outomaticaaly 
# create the file like :

f = open("tejas.py","a")
f.close()

f = open("tejas1.py","a")
f.close()                    #21:01


# w+ mode using write and overwrite this is *truncate* mines delete file data 
f = open("file save data.py","w+") #use a+
f.write("abc")
print(f.read())
f.close()

# r+ using in read and overwrite the data pointer starat starting no truncate
f = open("file save data.py","r+") #use a+
f.write("abc")
print(f.read())
f.close()

#append mode a+ add and overwrite the data pointer start ending no truncate
f = open("file save data.py","a+") #use a+
# f.write("abc")
print(f.read())
f.write("abc")
f.close()