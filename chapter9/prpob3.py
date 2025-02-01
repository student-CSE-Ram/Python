word = "donkey"

with open("dnk.txt") as f:
    content = f.read()

with open("dnk.txt","w")as f:
    f.write(content.replace(word,"#" * len(word)))
    
