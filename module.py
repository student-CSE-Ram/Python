def myFunc():
    print("Hello this is a normal function")

myFunc()
print(__name__)

# the inbuilt function __name__ show the location from where the file is opened whether by its own address or some other address (imported in other file)
# the below if statement decides that the above function if opening in other file or not in this case if we run this function fnction from this file location the function will run because it matches the condition and if the function is opened in some other file this will not work 
 
if(__name__ == "__main__"):
    print("this file is opened in its own location not from any other imported location")
    myFunc()
    print(__name__)
