
#dictionay are store a data key values in pair keys value like:
#dictionary is mainly string format printed every value like list tuple print in value but key value print only 
#string int float tuple also possible because this is immutable 
#dictionary store mainly keys immutable every and values everything like mutable immutable also :
#no order in dictionary becaus list tuple string like indexing than calculate spases and value but dic not counted
#because dic is mutable mean posible in value in dic  don,t allow dublicate keys 
 
dict = {
    "name" : "Tejas badgujar", #right side values and left side keys so than value store everytype but keys only 
    "age" : 21,                  #store immutable values like string,int tuple that like and so on :
    "marks" : 74.20,              #and last in value last quama compulsory every value 
    "num" : ["10","20","30","40"],
    "birtsh name" : ("Tejas","Badgujar"),
    "is_adult" : True

}
dict["name"] = "tejas Subhash badgujar"
dict["count"] = "numbers"
print (type(dict))
print(dict)

#like null dictionary

null_dict = {} #print empty dict add also possible like :
null_dict["name"] = "tejas badgujar"
print(null_dict)

#nested dictionary like :

student = {
    "name" : "tejas Badgujar",
    "subjects" : {
        "english" : 94,   #these like nesting is dictionary
        "it" : 96,
    }
}    
print(student["subjects"]["it"])