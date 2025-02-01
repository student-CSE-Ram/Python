# def goodDay(name,ending):
#     print(f"Good day, {name} {ending}")

# goodDay("Ram","Jai ho")

def goodDay(name,ending= "Radhe Radhe"): # here we set a default value if we pass some parameter in place of ending then it will print that parameter otherwise it will print "Radhe Radhe" the default value of the parameter
    print(f"Good day, {name} {ending}")

goodDay("Ram","Jai ho")