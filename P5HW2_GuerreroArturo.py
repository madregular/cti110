# Create a math quiz with a menu selection for subtraction or addition
# 07/09/2022
# CTI-110 P5HW2 - Math Quiz
# Arturo Guerrero
#

# import random to generate random integer
import random

# define main_menu function
def main_menu():
    print("MAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit\n")

# define math table function for output
def table(choice_input):
    if choice_input == 1:
        print(f"  {num1}\n"
              f"+ {num2}")
    elif choice_input == 2:
        print(f"  {num1}\n"
              f" + {num2}")
    return

# define math_check to check if the user's guess is too low or two high
def math_check(guess):
    guess_count = 0
    while guess_count >= 0:
        if guess < answer:
            print("Sorry, guess is too low.\n")
            guess = guess = int(input("try again: "))
            guess_count += 1
        elif guess > answer:
            print("Sorry, guess is too high.\n")
            guess = guess = int(input("try again: "))
            guess_count += 1
        else:
            print("Congratulations!!!! you answer is correct.")
            print(f"Number of guesses: {guess_count}\n")
            guess_count = -1
            break
    return


# generate random numbers
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)


# show welcome header and output the menu
# ask the user for a menu choice
value = 0
while value == 0:
    print("Welcome to Math Quiz")
    main_menu()
    user_choice = int(input("Please choose one of the following options: "))
    # when the user enters 1, execute program and adds the numbers, ask user for input and display results
    if user_choice == 1:
        table(user_choice)
        answer = num1 + num2
        guess = int(input("Please enter answer: "))
        math_check(guess)

    # when the user enters 2, execute program and subtract the numbers, ask user for input and display results
    elif user_choice == 2:
        table(user_choice)
        answer = num1 - num2
        guess = int(input("Please enter answer: "))
        math_check(guess)

    # when the user enters 3, exit the program
    elif user_choice == 3:
        print("Thank you for playing...")
        print("Bye")
        value = 1

    # return error is another value is chosen
    while 0 < user_choice > 3:
        print("Error: Incorrect menu option chosen")
        user_choice = int(input("Please try again.: "))

