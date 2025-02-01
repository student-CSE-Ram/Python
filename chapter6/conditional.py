a = int(input("Enter your age :"))
# if elif else ladder 
if(a>=18):
    print("You are an adult now.")
    print("You can vote")
elif(a>10 and a<18):
    print("You are a teenager.")

elif(a<10):
    print("Hello kid!")

else:
    print("Something went worng, Plese enter your age again")

