#lets make a rock paper scissor game
import random
import time
print("Welcome to the Rock Paper Scissor Game")
print("You will be playing against the computer")
print("You will be given 3 chances to win")
print("Lets start the game")
print("Rock Paper Scissor")
print("Rock crushes Scissor")
print("Scissor cuts Paper")
print("Paper covers Rock")
print("Lets start the game")
print("You will be given 3 chances to win")

#lets make a list of choices
choices = ["Rock", "Paper", "Scissor"]
#lets make a variable for the computer choice
computer_choice = random.choice(choices)
#lets make a variable for the user choice
user_choice = input("Enter your choice: ")
#lets make a variable for the number of chances
chances = 3
#lets make a variable for the number of chances used
chances_used = 0
#lets make a variable for the number of chances left
chances_left = chances - chances_used
#lets make a variable for the number of chances used
chances_used = chances_used + 1
#lets make a variable for the number of chances left
chances_left = chances - chances_used

#lets make a while loop
while chances_left > 0:
    #lets make a if statement
    if user_choice == computer_choice:
        print("Its a tie")
        print("Computer choice: ", computer_choice)
        print("Your choice: ", user_choice)
        print("You have used", chances_used, "chances")
        print("You have", chances_left, "chances left")
        print("Lets start the game again")
        print("You will be given 3 chances to win")
        #lets make a variable for the computer choice
        computer_choice = random.choice(choices)
        #lets make a variable for the user choice
        user_choice = input("Enter your choice: ")
        #lets make a variable for the number of chances used
        chances_used = chances_used + 1
        #lets make a variable for the number of chances left
        chances_left = chances - chances_used
    #lets make a elif statement
    elif user_choice == "Rock" and computer_choice == "Scissor":
        print("You win")
        print("Computer choice: ", computer_choice)
        print("Your choice: ", user_choice)
        print("You have used", chances_used, "chances")
        print("You have", chances_left, "chances left")
        print("Lets start the game again")
        print("You will be given 3 chances to win")
        #lets make a variable for the computer choice
        computer_choice = random.choice(choices)
        #lets make a variable for the user choice
        user_choice = input("Enter your choice: ")
        #lets make a variable for the number of chances used
        chances_used = chances_used + 1
        #lets make a variable for the number of chances left
        chances_left = chances - chances_used
    #lets make a elif statement
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You win")
        print("Computer choice: ", computer_choice)
        print("Your choice: ", user_choice)
        print("You have used", chances_used, "chances")
        print("You have", chances_left, "chances left")
        print("Lets start the game again")
        print("You will be given 3 chances to win")
        #lets make a variable for the computer choice
        computer_choice = random.choice(choices)
        #lets make a variable for the user choice
        user_choice = input
("Enter your choice: ")
