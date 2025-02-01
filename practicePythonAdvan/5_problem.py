from typing import List, Tuple, Dict

n = int(input("Enter a number :"))

table = [n*i for i in range(1,11)]

with open("5_table.txt","a") as f:
    f.write(str(table) + "\n")