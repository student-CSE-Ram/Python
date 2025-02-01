'''this is an example of file open and file read and write '''


# f = open("plain.txt","r")
# data = f.read()
# print(data)
# f.close()


str = "this is an string thAT is created in this file"

f = open("plain2.txt","w")
f.write(str)

f.close()