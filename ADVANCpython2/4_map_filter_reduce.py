from functools import reduce

# Example of map function

l = [1,2,3,4,5,6]

square = lambda n: n*n

sqList = map(square,l)
print(list(sqList))

# Example of filter function 

def even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(even,l)  # the filter function take two argument one is a function and other one is a list
print(list(onlyEven))

# Example of reduce function

def sum(a,b):
    return a+b

print(reduce(sum,l)) # he reduce function will also tak two argument one is the function and other is list in this function(sum) the list will be added by there next number untill it will reach at the end