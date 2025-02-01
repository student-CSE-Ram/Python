li = [123,54,45,65,75,90,87,25]

def div5(n):
    if(n%5 == 0):
        return True
    return False

divisble = filter(div5,li)
print(f"The number that are divisble by 5 are {list(divisble)}")
    