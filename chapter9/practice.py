# wap to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'

f = open("poems.txt")

line = f.readline()
if("twinkle" in line):
    print(line)
else:
    print("The word twinkle not found in the line")

f.close()
