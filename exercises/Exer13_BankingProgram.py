"""
Exercise 12: Banking Program

"""
import time

def ui_get_user_info():
    print("*"*26)
    print("Welcome to bank of Ustio!")
    print("Please Enter your User Info")
    print("*"*26)

def get_user_info():
    first_name = input("Enter your first name: ")
    middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")
    bank_id = input("Enter your Bank ID: ")
    print("*"*26)
    return first_name, middle_name, last_name, bank_id

def display_user_info(first_name, middle_name, last_name, bank_id):
    print(f"Name: {first_name} {middle_name}. {last_name} \nBank ID: {bank_id}")
    
def get_choice():
    while True:
        try:
            return int(input("\nEnter your choice: "))
        except ValueError:
            display_mgs("Please enter a valid choice (1/2/3/4)")

def choice_logic(choice,balance):
    if choice == 1:
        display_balance(balance)
        return balance, True
    elif choice == 2:
        return deposit(balance), True
    elif choice == 3:
        return withdraw(balance), True
    elif choice == 4:
        display_mgs("Exiting...")
        time.sleep(1)
        return balance,False
    else:
        display_mgs("Invalid Choice!")
        time.sleep(1)
        return balance, True

def display_balance(balance,amount=None,transaction:str=None):
    if transaction=="deposit":
        display_mgs(f"Successfully deposited ${amount:.2f}")
    elif transaction == "withdraw":
        display_mgs(f"Successfully withdrawn ${amount:.2f}")
        
    display_mgs(f"Your Bank Balance: ${balance:.2f}")


    time.sleep(1)

def get_amount(msg:str):
    while True:
        try:
            print()
            amount = float(input(f"Enter Amount {msg}: $"))
            return amount
        except ValueError:
                display_mgs("Invalid Input!")

def deposit(balance):
    
    amount = get_amount("to be deposit")

    if amount <= 0:
        display_mgs("That's not a valid amount!")
        time.sleep(1)
        return balance
    
    balance += amount
    display_balance(balance,amount,"deposit")
    return balance 


def withdraw(balance):
    amount = get_amount("to be withdrawn")

    if amount <= 0: 
        display_mgs("Amount must not be less than 0!")
        time.sleep(1)
        return balance
    
    elif amount > balance:
        display_mgs("Insufficient balance!")
        time.sleep(1)
        return balance

    balance -= amount
    display_balance(balance,amount,"withdraw")
    return balance

def display_mgs(msg:str):
    print(f"\n{msg}")

def main():
    ui_get_user_info()
    first_name, middle_name, last_name, bank_id = get_user_info()
    balance = 0.0
    is_running = True
    
    while is_running:
        print()
        print("*"*26)
        print("Welcome to Bank of USTIO")
        display_user_info(first_name, middle_name, last_name, bank_id)
        print("*"*26)
        print("[1] Show Balance")
        print("[2] Deposit")
        print("[3] Withdraw")
        print("[4] Exit")
        print("*"*26)
        choice=get_choice()
        balance,is_running= choice_logic(choice,balance)
         
if __name__ == '__main__':
    main()