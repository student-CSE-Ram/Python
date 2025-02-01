import random
n = random.randint(1,50)
guesses = 1
a = -1


while(a != n):
    
    a = int(input("Guess the number :"))
    if(a > 50):
        print("Enter the number less than 50")
    elif(a>n):
        print("Enter the lower number")
        guesses+=1
    elif(a<n):
        print("Enter higher number pls")
        guesses+=1

print(f"You have guessed the number {n} in {guesses} attempts")
