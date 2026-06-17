import random

def get_die_number():
    while True:
        numb_die = input("Enter number of dices: ")
        if numb_die.isdigit():
            return int(numb_die)
        print("You've enter wrong choice")

def roll_dice(numb_die, dices):
    for die in range(numb_die):
        dices.append(random.randint(1,6))
    return dices

def display_dice(dices,dice_arts,numb_die):
    for die in range(numb_die):
        for line in dice_arts.get(dices[die]):
            print(line)

def total_dice(dices,total):
    for die in dices:
        total +=die
    return total

def display_total_dice(total):
    print(f"Total of Dices: {total}")

dice_arts={
    1: (
        "┌───────────────┐",
        "│               │",
        "│               │",
        "│       ●       │",
        "│               │",
        "│               │",
        "└───────────────┘"
        ),

    2: (
        "┌───────────────┐",
        "│               │",
        "│   ●           │",
        "│               │",
        "│           ●   │",
        "│               │",
        "└───────────────┘"
        ),

    3: (
        "┌───────────────┐",
        "│               │",
        "│   ●           │",
        "│       ●       │",
        "│           ●   │",
        "│               │",
        "└───────────────┘"
        ),

    4: (
        "┌───────────────┐",
        "│               │",
        "│   ●       ●   │",
        "│               │",
        "│   ●       ●   │",
        "│               │",
        "└───────────────┘"
        ),

    5: (
        "┌───────────────┐",
        "│               │",
        "│   ●       ●   │",
        "│       ●       │",
        "│   ●       ●   │",
        "│               │",
        "└───────────────┘"
        ),

    6: (
        "┌───────────────┐",
        "│               │",
        "│   ●       ●   │",
        "│   ●       ●   │",
        "│   ●       ●   │",
        "│               │",
        "└───────────────┘"
        )
}

dices=[]
total=0

numb_die = get_die_number()
dices = roll_dice(numb_die,dices)
display_dice(dices,dice_arts,numb_die)
total = total_dice(dices,total)
display_total_dice(total)



