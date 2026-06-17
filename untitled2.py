"""
6. Shopping Cart

Create a simple shopping cart:

Ask the user to enter item names.
Ask for the item price.
Continue until the user enters "q".
Display all items and the total price.
"""
def get_str(msg: str):
    while True:
        try:
            return str(input(f"{msg}"))
        except ValueError:
            print("Invalid input. Enter a number.")

def get_int(msg:str):
    while True:
        try:
            return int(input(f"{msg}"))
        except ValueError:
            print("Invalid Input")

def init_shopping_list():
    return []

def init_price_list():
    return []

def add_item_to_cart(item,price,shopping_cart,price_list):
    shopping_cart.append(item)
    price_list.append(price)
    return shopping_cart,price_list



def display_shopping_cart(shopping_cart, price_list):
    for item, price in zip(shopping_cart,price_list):
        print(f"Item: {item}\nPrice: ${price}")

def display_shopping_cart_total(price_list):
   total = sum(price_list)
   print(f"Total Cost: {total}")

def stop_shopping():
    return False if input("enter q to stop shopping ").lower() == 'q' else True


def main():
    shopping_cart = init_shopping_list()
    price_list = init_price_list()
    is_running = True


    while is_running:
        item = get_str("Enter items: ")
        price = get_int("Enter price: ")
        shopping_cart,price_list = add_item_to_cart(item,price,shopping_cart,price_list)
        is_running = stop_shopping()
    display_shopping_cart(shopping_cart,price_list)
    display_shopping_cart_total(price_list)



"""
8. Caesar Cipher

Encrypt a message by shifting each letter by a user-specified amount.

Example:

Text: hello
Shift: 3
Output: khoor

"""
import string

def init_cipher_list():
    chars = list(string.ascii_letters)
    return chars

def cipher_logic(chars,original_word,cipher_shift):
    ciphered_word = ""
    encrypt = lambda char: chars[
        (chars.index(char) + cipher_shift) % len(chars)
    ]

    for word in original_word:
        if word in chars:
            ciphered_word += encrypt(word)
        else:
            ciphered_word += word
    return ciphered_word

def display_output(ciphered_word,original_word, cipher_shift):
    print(f"Original Word: {original_word}\nShifts: {cipher_shift}\nOutput: {ciphered_word}")



def caesar_cipher_main():
    original_word = get_str("Enter word to cipher: ")
    cipher_shift = get_int("Enter number of shifts: ")
    chars= init_cipher_list()
    ciphered_word = cipher_logic(chars,original_word,cipher_shift)
    display_output(ciphered_word,original_word, cipher_shift)
    


def init_words():
    return ["Worlds","Coconut","Apple"]

def word_picker(word):
    import random
    picked_word = random.choice(word)
    return picked_word

def hangman_logic(picked_word,guess,guessed_letter,is_running,hint):
    if guess in picked_word:
        for i in range(picked_word):
            if picked_word[i] == guess:
                hint[i] = guess

    pass



def display_hint(hint):
    print(" ".join(hint))

def hang_man_main():
    word = init_words()
    picked_word = word_picker(word)
    hint = ['_'] * len(picked_word)
    guessed_letter = set()
    is_running = True

    while True:
        display_hint(hint)
        guess_letter = get_str("Enter a Letter: ")
"""
# Read the sentence
sentence = input().strip()

# Reverse the words and print
splitted_sentence = sentence.split()

for i in range(len(splitted_sentence)-1,-1,-1):
    print(splitted_sentence[i],end=" ")
"""


n = int(input())

run = True

while run:
    if n == 1:
        print("Yes")
        run = False
    elif n % 2 == 0 and n > 1:
        n //= 2
    else:
        print("No")
        run = False