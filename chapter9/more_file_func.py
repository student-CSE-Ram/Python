# f = open("plain.txt")
# # lines = f.readlines() read the complete lines 
# # print(lines,type(lines))

# line1 = f.readline() # read the first line and read line by  line
# print(line1)
# f.close()


# str = "Radhe Radhe "

# f = open("plain2.txt","a")
# f.write(str)
# f.close()

with open("plain.txt","r") as f:
    print(f.read())


# this is the best way to open a file and read or write something , in this you don't have to use closing tag explicitly
