a = (1,2,3,45,232,False,"Ram",45)
# print(type(a))
# print(a)

no = a.count(45) # return the no of items present in the tupple(list)
# print(no)

i = a.index(45) # return the index at where the the item is present 
# print(i)

# a[3] = 54  # this line will not work because tupple are immuatable
# print(a)  #tupple are immuteable just like strings  



marks = []

f1 = int(input(("Enter marks name :")))
marks.append(f1)

f2 = int(input(("Enter marks name :")))
marks.append(f2)

f3 = int(input(("Enter marks name :")))
marks.append(f3)

f4 = int(input(("Enter marks name :")))
marks.append(f4)

f5 = int(input(("Enter marks name :")))
marks.append(f5)

f6 = int(input(("Enter marks name :")))
marks.append(f6)

marks.sort()
print(marks)