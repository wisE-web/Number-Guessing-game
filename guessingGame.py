import random
print("NUMBER GUESSING GAME")
number=random.randint(1,9)
chances=0
while chances < 5:
    guess=int(input("enter your guess:"))
    if guess == number:
        print("YOU WON")
        break
    elif guess < number: 
        print("you guess is too low")
    else: 
        print("your guess is to high")
    chances+=1
if not chances < 5:
    print("you lose")
