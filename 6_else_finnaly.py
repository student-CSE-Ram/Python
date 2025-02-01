# try:
#     a = int(input("Enter a number :"))
#     print(f"The number you entered is {a}")


# except ValueError as v:  
#     print("The value you entered is not integer type pls enter a valid input.")

# finally:
#     print("This is a finally block that is not dependent on try and except block")

# print("Thank you")




def main():
    try:
        a = int(input("Enter a number :"))
        print(f"The number you entered is {a}")


    except ValueError as v:  
        print("The value you entered is not integer type pls enter a valid input.")

   
        print("This is a finally block that is not dependent on try and except block")


main()