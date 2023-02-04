#guess the number game
import random
print("Hello. What is your name?")
name = input()#input() function is used to take input from the user
secretNumber = random.randint(1, 20) #random number between 1 and 20
print("Well, " + name + ", I am thinking of a number between 1 and 20.")
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7 , 1):#range(start, stop, step)
    print("Take a guess!")#this is the statement that will be printed
    guess = int(input())
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break # This condition is the correct guess!
if guess == secretNumber:
    print("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
    