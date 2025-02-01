s = {12,34,34,34,76,76,89,90} # this an example of set.Set remove the repeatet data of the list
#e  = {} #this is an empty dictionary so don't use this syntax to create an empty set
e = set() #this is an empty set

print(s,type(s))

# sets method

s1 = {1,54,67,12}
s2 ={1,56,87,12}
print(s1.union(s2))
print(s1.intersection(s2))