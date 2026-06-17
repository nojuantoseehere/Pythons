
import random

def player_choice(options):
    while True:
        player = input("Enter your choice (Rock, Paper, Scissor): ").capitalize()
        if player in options:
            return player
        print("You've enter a wrong choice!")

def display_entered_choice(player,computer):
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    
def rock_paper_scissor_logic(player,computer):

    if player == computer:
        return "tie"
    elif player == "Rock" and computer == "Scissor":
        return "player"
    elif player == "Paper" and computer == "Rock":
        return "player"
    elif player == "Scissor" and computer == "Paper":
        return "player"
    else:
        return "computer"

def display_feedback(is_won):

    if is_won == "tie":
        print(f"It's a Tie!")
    elif is_won == "player":
        print(f"Player Won!")
    elif is_won =="computer":
        print(f"Computer Won!")

def play_again():
    if input("Play again? Y/N: ").upper() == "Y":
        return True
    return False

def main():
    options = ("Rock","Paper","Scissor")
    player = None
    computer = random.choice(options)
    is_active = True

    while is_active:
        player = player_choice(options)
        display_entered_choice(player,computer)
        is_won = rock_paper_scissor_logic(player,computer)
        display_feedback(is_won)
        is_active = play_again()

if __name__ == '__main__':
    main()
