#  in the python genrally you don't need to define the type of the variable but in the some case it become difficult for the other coder if they use your code so we define the type of the variable in such ways 

from typing import List, Tuple, Dict

nums :List[int] = [5,67,87,90,675]

print(type(nums))

name : str = "Ram"

def sum(a:int,b:int) -> int:
    return a+b


# add = sum(65,45)
# print(add)