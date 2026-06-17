import random
from Exer13_BankingProgram import display_mgs


def init_word():
    word = ['word']
    return word
def init_hangman_art():
    hangman_art ={
        0 : (
             "   ",
             "   ",
             "   ",
             ),

        1 : (
             " O ",
             "   ",
             "   ",
             ),

        2 : (
             " O ",
             " | ",
             "   ",
             ),

        3 : (
             " O ",
             "/| ",
             "   ",
             ),

        4 : (
             " O ",
             "/|\\",
             "   ",
             ), 

        5 : (
             " O ",
             "/|\\",
             "/  ",
             ),

        6 : (
             " O ",
             "/|\\",
             "/ \\ ",
             )
    }
    return hangman_art


def word_picker(word):
    picked_word = random.choice(word)
    return picked_word

def get_guess_letter():
    while True:
        try:
            guess_letter = input("Enter letter to guess: ")
            return guess_letter
        except ValueError:
            display_mgs("Invalid Input")
            

def hangman_logic(
        picked_word,
        guess_letter,
        hint,
        guessed_letter,
        wrong_guesses,
        is_running):

    if guess_letter in guessed_letter:
        display_mgs(f"{guess_letter} is already guessed")
        return hint, wrong_guesses, is_running

    guessed_letter.add(guess_letter)

    if guess_letter in picked_word:
        for i in range(len(picked_word)):
            if picked_word[i] == guess_letter:
                hint[i] = guess_letter
    else:
        wrong_guesses += 1

    if "_" not in hint:
        display_picked_word(picked_word)
        display_mgs("You've Won!")
        is_running = False

    if wrong_guesses >= 6:
        display_mgs("You've Lost!")
        display_mgs(f"The word was: {picked_word}")
        is_running = False

    return hint, wrong_guesses, is_running




        



def display_hint(hint):
    print(' '.join(hint))

def display_picked_word(picked_word):
    print(' '.join(picked_word))

def display_hangman_art(hangman_art,wrong_guesses):
    for line in hangman_art.get(wrong_guesses):
        print(line)





def main():
    word = init_word()
    hangman_art = init_hangman_art()
    picked_word = word_picker(word)
    hint = ['_'] * len(picked_word)
    guessed_letter = set()
    wrong_guesses = 0
   
    is_running = True
    while is_running:

        display_hangman_art(hangman_art,wrong_guesses)
        display_hint(hint)
        guess_letter = get_guess_letter()
        hint,wrong_guesses,is_running = hangman_logic(picked_word,guess_letter,hint, guessed_letter,wrong_guesses,is_running)


if __name__ == "__main__":
    main()

