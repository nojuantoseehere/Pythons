"""
Exercise 11 Retake
Create a Head or Tail coin program
topic applied, if else, while, for, data collections
"""

import random


def get_number_of_coin():
    """
    get the value of numbOfCoins
    proceeds to a while loop if a user enters a string which is check by isdigits function
    if true return in type converted var into int
    else goes back into while loop
    """
    while True:
        numbOfCoins = input("Enter your desire number of coins: ")
        if numbOfCoins.isdigit():
            return int(numbOfCoins)
        print("Enter an Number!")

def flip_coin(numbOfCoins,coins):
    for _ in range(numbOfCoins):
        coins.append(random.randint(0,1))
    return coins

def display_coin(numbOfCoins, coin_art,coins):
    for coin in coins:
        for line in coin_art[coin]:
            print(f"{line}")


def calculate_total_coin(coins):
    return sum(coins)

def display_total_coin(total,numbOfCoins):
    print(f"Total Value of {numbOfCoins} Coins is: {total:00}\nTail equates to 0 while head is 1")

def play_again():
    return input("Play again? Y/N: ").upper() == "Y"
    


coin_art = {
    0: (
        "   _____",
        " /       \\",
        "|  TAILS  |",
        " \\ _____ /",
    ),

    1: (
        "   _____",
        " /       \\",
        "|  HEADS  |",
        " \\ _____ /",
    )
}


is_running = True
while is_running:
    coins = []
    numbOfCoins = get_number_of_coin() # Get the value of variable numbOfCoins
    coins = flip_coin(numbOfCoins,coins) # get the randomize values of coins var based on the numbOfCoins var
    display_coin(numbOfCoins, coin_art, coins) # display the ascii coins based on the numbOfCoins var
    total = calculate_total_coin(coins) # calculate the randomize values of coins var
    display_total_coin(total,numbOfCoins) # display the total var value 
    is_running = play_again() # get input from user, if input equates to Y return true to continue else return False to End