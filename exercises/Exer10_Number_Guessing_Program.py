"""
Exercise#9 Create a number guessing game
Topics applied: functions, if-else, while, and random module


"""

import random

def get_range_number():
    low_bracket = int(input("Enter the Lowest Range of Number: "))
    high_bracket = int(input("Enter the Highest Range of Number: "))
    return low_bracket, high_bracket

def randomizer(low_bracket, high_bracket):
    random_numb = random.randint(low_bracket,high_bracket)
    return random_numb

def get_guess_number(low_bracket, high_bracket):
    while True:
        guess = input(f"Enter your guess number from {low_bracket} to {high_bracket}: ")
        if guess.isdigit():
            return int(guess)
        print("Wrong input! Please Enter a number!")

def guess_and_randomizer_logic(random_numb,guess,low_bracket,high_bracket,guesses):
    
    if guess < low_bracket or guess > high_bracket:
        return (
                True,
                "Your Guess Number is out the set range!\n"
                f"Enter a guess number under this range {low_bracket} - {high_bracket}"
                )
    
    elif guess < random_numb:
        return (
                True,
                "Your Guess number is lower than the random number!\n"
                "Pls Try again uwu"
                )
    elif guess > random_numb:
        return (
                True,
                "Your Guess number is higher than the random number!\n"
                "Pls Try again uwu"
                )
    else:
        return (
                False,
                "You Guessed the Correct Number!\n"
                f"Correct Number: {random_numb}\n"
                f"Number of Guesses: {guesses + 1}"
                )

def display_feedback(result:str):
    print(f"{result}")


is_running = True
guesses = 0
print("=== Exercise 9 (Number Guessing Game) ===\n")
print()
low_bracket, high_bracket = get_range_number()
random_numb = randomizer(low_bracket, high_bracket)

while is_running:
    guess = get_guess_number(low_bracket,high_bracket)
    print()
    status,result = guess_and_randomizer_logic(random_numb, guess,low_bracket,high_bracket,guesses)
    guesses += 1
    display_feedback(result)
    is_running = status