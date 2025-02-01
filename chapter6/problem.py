
# this is a simple program to detect the spam comment in a program

p1 = "click here"
p2 = "Login"
p3 = "Hello moto"

message = input("Enter a comment :")

if (p1 in message) or (p2 in message) or (p3 in message):
    print ("This is a spam comment")
else:
    print("This is a valid comment")