#  if we're not sure that the program will through an error then we'll put that code in try block 

try:
    a = int(input("Enter a number :"))
    print(f"The number you entered is {a}")

# this is exception handling , if we didn't wrote the block except then the remaining program would not be executed but now the remaining program will execute properly and we can print the output whatever we want.

except ValueError as v:  
    print("The value you entered is not integer type pls enter a valid input.")


print("Thank you")
