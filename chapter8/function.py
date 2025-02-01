#function definition 

def avg():
    a=int(input("Enter the number :"))
    b=int(input("Enter the number :"))
    c=int(input("Enter the number :"))

    average = (a+b+c)/3
   # print(f"The average is {average}")
    return average   # this is a return statement
# function calling 
a=avg()
print(a)