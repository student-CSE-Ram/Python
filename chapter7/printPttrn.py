
'''
   *
  ***
 *****

'''

n = int(input("Enter the number: "))

for i in range(1,n+1):
    print(" " * (n-i),end="") # here "end" restrict the print function to take the code into the new line
    print("*" * (2*i-1),end="")
    print("")

    