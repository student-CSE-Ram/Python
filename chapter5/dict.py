#dictionary & sets

marks = {
    "Ram":1205,
    "nitesh":1150,
    "Shivankar":1100
}
#print(marks,type(marks))

marks["Shivankar"] = 1111 # this line shows that the dictionary are muteable 
print(marks)

print(marks.items())  #display the key value pair in form of tupple 
print(marks.keys()) # display the number of keys present in it
print(marks.values())  # display the values of each key
marks.update({"Shivankar":1050,"Shivam":1000}) # this line update the dictionary if we have make change in any present key then it will change the present key and if we want to add any new key value pair then it will also add the new key value pair
print(marks)

#print(marks.get["Ram"])  # both line will give the same output but if there was an error in the key name then the first line will give 'none' and second line will give an error
#print(marks["Ram"])

# int 1 and float 1.0 will be same in python 


#in an empty dict add some friends name as key and input their lang as value 

