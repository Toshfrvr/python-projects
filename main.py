import random
import math

# --- Guess the Number Game ---
def guess_the_number():
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("\nWelcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
    else:
        print(f"Out of attempts! The number was {secret_number}.")

# --- Simple Calculator ---
def simple_calculator():
    print("\nSimple Calculator")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid operator. Please choose from +, -, *, /.")

# --- Prime Number Checker ---
def is_prime():
    print("\nPrime Number Checker")
    try:
        number = int(input("Enter a positive integer: "))
        if number < 2:
            print("Not a prime number (must be 2 or greater).")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    i = 2
    is_prime_flag = True

    while i <= number // 2:
        if number % i == 0:
            is_prime_flag = False
            break
        i += 1

    if is_prime_flag:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

# --- Shape Calculator ---
def area_of_square(side):
    return side * side

def perimeter_of_square(side):
    return 4 * side

def area_of_rectangle(length, width):
    return length * width

def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def area_of_circle(radius):
    return math.pi * radius * radius

def circumference_of_circle(radius):
    return 2 * math.pi * radius

def area_of_triangle(base, height):
    return 0.5 * base * height

# --- Calculate Grade Function ---
def calculate_grade(score):
    """Returns the letter grade based on the score."""
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return "Invalid score. Please enter a value between 0 and 100."

# --- Check if a Number is Positive or Negative ---
def check_positive_or_negative(number):
    """Determines whether a number is positive, negative, or zero."""
    if number > 0:
        return f"{number} is a positive number."
    elif number < 0:
        return f"{number} is a negative number."
    else:
        return "The number is zero, which is neither positive nor negative."

# --- Main Menu ---
def menu():
    print("\nChoose a program to run:")
    # print("1. Guess the Number Game")
    # print("2. Simple Calculator")
    # print("3. Prime Number Checker")
    # print("4. Shape Calculator")
    # print("5. Calculate Grade")
    print("6. Check Positive or Negative")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        guess_the_number()
    elif choice == "2":
        simple_calculator()
    elif choice == "3":
        is_prime()
    elif choice == "4":
        print("\nChoose a shape:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Triangle")
        shape_choice = input("Enter your choice (1-4): ")

        if shape_choice == "1":
            side = float(input("Enter side length of square: "))
            print("Area:", area_of_square(side))
            print("Perimeter:", perimeter_of_square(side))

        elif shape_choice == "2":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            print("Area:", area_of_rectangle(length, width))
            print("Perimeter:", perimeter_of_rectangle(length, width))

        elif shape_choice == "3":
            radius = float(input("Enter radius: "))
            print("Area:", area_of_circle(radius))
            print("Circumference:", circumference_of_circle(radius))

        elif shape_choice == "4":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            print("Area:", area_of_triangle(base, height))
            print("Note: Perimeter requires all 3 sides")

        else:
            print("Invalid choice. Please try again.")

    elif choice == "5":
        try:
            score = float(input("\nEnter the score (0-100): "))
            print(f"The grade is: {calculate_grade(score)}")
        except ValueError:
            print("Invalid input. Please enter a valid score.")

    elif choice == "6":
        try:
            number = float(input("\nEnter a number to check if it's positive or negative: "))
            print(check_positive_or_negative(number))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print("Invalid choice. Please run the program again and enter a number between 1 and 6.")

# Run the main menu
menu()

import random

def play_rps():
    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Choose rock, paper, or scissors (or type 'quit' to exit): ").lower()
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"You chose {user_choice}, computer chose {computer_choice}.")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
        else:
            print("You lose!")


if __name__ == "__main__":
    play_rps()
