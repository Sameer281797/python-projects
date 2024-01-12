print("Guess the number (1 - 10)")
import random

while True:
    randnumber = random.randint(1, 10)
    userguess = None
    guesses = 0
    
    while (userguess != randnumber):
        userguess = int(input("Enter your guess: "))
        guesses += 1
        
        if (userguess == randnumber):
            print("You guessed it right!")
            print(f"You guessed the number in {guesses} guesses")
        else:
            if (userguess > randnumber):
                print("You guessed it wrong! Enter a smaller number!")
            else:
                print("You guessed it wrong! Enter a larger number!")
    
    newgame = input("Do you want to play again? (yes/no): ")
    if newgame.lower() != 'yes':
        break