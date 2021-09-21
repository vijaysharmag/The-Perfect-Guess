# project 2 The Perfect Guess

# vijaysh318@gmail.com

import random
randNumber = random.randint(1, 100)
# print(randNumber)
guesses = 0
userGuess = None
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess == randNumber):
        print("you guessed it right!")
    else:
        if(userGuess>randNumber):
            print("you gusses it wrong!, Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())
if(guesses<hiscore):
    print("you have just broken the hiscore")

    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
