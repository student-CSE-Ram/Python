
with open("log.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if("python" in line):
        print(f"The word python is present in the paragraph at line no: {lineno}")
        break
    lineno +=1
else:
    print("The word python is not present in the paragraph")