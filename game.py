## Number guessing game

# version 1
# 1. user can start the game
# 2. play for one guess (guessing correct number is win and wrong answer is loss) (complete game)
# 3. should not terminate, should keep it continuing

# import random

# while True:
#     s = input("type 'start' to play the game: ").lower()
#     if s=="start":
#         print("game started")
#         NUM_SET  = random.randint(0,9)
#         c = 0
#         while c<1: 
#             try:
#                 guess = int(input("guess a number: "))
#                 if NUM_SET == guess:
#                     print("win")
#                     c = 1
#                 else:
#                     print("lose")
#                     c = 1
#             except:
#                 print("please give only numbers")   
#     else:
#         break


# version 1.5
# only 7 guess should be there for one game

import random
money = 200
while True:
    s = input("type 'start' to play the game: ").lower()
    if s=="start":
        diff = input("select difficulty level to play the game:\n'easy', 'medium' or 'hard': ").lower()
        if diff == "easy":
            NUM_SET  = random.randint(0,9)
            c = 7
            reward = 5
            print("game started")
        elif diff=="medium":
            NUM_SET  = random.randint(0,15)
            c = 8
            reward = 15
            print("game started")
        elif diff == "hard":
            NUM_SET  = random.randint(0,20)
            c = 9
            reward = 50
            print("game started")
        print(NUM_SET)
        while c>0: 
            try:
                guess = int(input("guess a number: "))
                if NUM_SET == guess:
                    print("you won the game")
                    money += reward
                    print(f"coins awarded: {reward}\nremaining coins: {money}")
                    break
                else:
                    if c>1:
                        c -= 1
                        print(f"not correct\ntry again****remaining number of guesses: {c}")
                    elif c==1:
                        c -= 1
                        print(f"money in account: {money}")
                        if money>10:
                            buy = input("do you want to buy a extra chance 'yes' or 'no': ")
                            if buy.lower() == "yes":
                                c+=1
                                money -= 10
                                print("thank you for the purchase")
                            else:
                                print("thank you for thinking")
                        else:
                            print("not enough money in account")
                            print("you lost")
                            break
            except:
                print("please give only numbers")   
    else:
        break
