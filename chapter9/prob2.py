import random

def game():
    print("You are playing a game ")
    score = random.randint(1,45)

    # fetch the high score
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    

    print(f"Your score: {score}")
    if(score>hiscore):
        # write this as a hiscore in the hiscore.txt file

        with open("hiscore.txt","w") as f:
            f.write(str(score))

    return score


game()










# def game():
#     print("You are playing a game...")
#     score = random.randint(1,50)

#     # fetching the hscore

#     with open("hiscore.txt")as f:

#        hiscore = f.read()
#        if(hiscore != ""):
#            hiscore = int(hiscore)
#         else :
#            hiscore = 0
        
           
        
           


      


        