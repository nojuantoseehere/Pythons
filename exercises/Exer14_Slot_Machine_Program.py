"""
Exercise 13
"""
import pygame
import time
from Exer13_BankingProgram import get_amount, display_mgs,display_balance



def get_balance():
    while True:
        try:
            return float(input("\nEnter your Balance: $"))
        except ValueError:
            display_mgs("Invalid Input")

def initialize_slot_machine():
    slot_machine = ['🔔','🍒','🍉','🍋','⭐']
    return slot_machine

def balance_amount_checker(balance,amount):

    if amount <= 0:
        display_mgs("That's not a valid amount!")
        return False

    elif amount > balance:
        display_mgs("Insufficient Funds!")
        return False

    return True


def spin_slot(slot_machine,balance):
    import random

    while True:
        amount = get_amount("to gamble")

        if balance_amount_checker(balance, amount):
            break
    
    spun_slot = [random.choice(slot_machine) for _ in range(3)]
  

    display_spun_slot(spun_slot)

    return  slot_machine_logic(spun_slot,balance,amount)

def slot_machine_sound(status:int):
    
    pygame.mixer.init()
    if status ==0:
        pygame.mixer.music.load("sounds/gamblecore.mp3")
        pygame.mixer.music.play()
        time.sleep(4)
    elif status ==1:
        pygame.mixer.music.load("sounds/slot_machine_jackpot.mp3")
        pygame.mixer.music.play()
        time.sleep(5)
    
    elif status ==2:
        pygame.mixer.music.load("sounds/lost.mp3")
        pygame.mixer.music.play()
        time.sleep(4)
    

    pygame.mixer.music.stop()


def display_spun_slot(spun_slot):
    slot_machine_sound(0)
    display_mgs("*" * 30)
    display_mgs("🎰  SLOT MACHINE  🎰")
    display_mgs("*" * 30)

    print(f"\n[ {spun_slot[0]} | {spun_slot[1]} | {spun_slot[2]} ]")

    display_mgs("*" * 30)





def slot_machine_logic(spun_slot,balance,amount):
    """
    If check if the expression len(set(spun_slot)) == 1 become true.
    The set function convert the spun_slot(list) into a set;
    the len get the length of converted set which returns 1 
    which is due to the nature of set of not allowing duplicates
    now the comparission == checks if the return value of len() is equal to 1
    
    """
    if len(set(spun_slot)) == 1:
        return payout(balance,amount,spun_slot,is_win=True)
    else:
        display_mgs("You've Lost!")
        return payout(balance, amount,spun_slot)

def payout(balance,amount,spun_slot,is_win=False):
    
    pay_out = {
        "🍋": 2,
        "🍉": 4,
        "🍒": 6,
        "🔔": 10,
        "⭐": 20,
    }
    if spun_slot == ["⭐", "⭐", "⭐"]:
        slot_machine_sound(1)

    if is_win:
        winnings = amount * pay_out[spun_slot[0]]
        balance += winnings
        display_mgs(f"You've Won ${winnings}")
        return balance
    else:
        balance -= amount
        display_mgs(f"You've Lost ${amount}")
        slot_machine_sound(2)
        return balance

def main():
    from Exer11_Rock_Paper_Scissor import play_again

    balance = get_balance()
    slot_machine = initialize_slot_machine()
    is_running = True

    while is_running:
        display_mgs("*"*26)
        print("Welcome To Python Slot Machine")
        print("Symbols: 🔔 🍒 🍉 🍋 ⭐ ")
        print("*"*26)
        display_balance(balance)
        balance = spin_slot(slot_machine,balance)
        display_balance(balance)
        is_running = play_again()


if __name__ == '__main__':
    main()