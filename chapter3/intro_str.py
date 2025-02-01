name = "Ramchandra"

print(name[0:6])
print(name[-6:-2]) # same as line 6  this is called negative slicing 

print(name[4:8]) # same as line 4
print(name[0:]) # this line means to slice from starting index to the last index(length-1)
print(name[:7]) 

#skiping in string 
print(name[1:6])
print(name[1:6:2])  #first we find the characters between 1 to 6th index and then we skip the number by 2 ex: the strings from 1 to 6 index is 'amcha' and then start from 'a' and we skip 'm' then second letter is 'c' same as 'h' is skipped then 'a' so the result is 'aca'

