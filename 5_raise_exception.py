a = int(input("Enter a number :"))
b = int(input("Enter Second number :"))

if(a == 0 or b== 0):
    raise ZeroDivisionError("The divident or divisible should not be zero.")
else:
    print(f"The division is {a/b}")