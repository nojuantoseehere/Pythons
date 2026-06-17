import os
import time

#Utility Func
def clear_screen():
    """Clears the console screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")

def clear_screen_delayed(n:int):
    """Clears the console screen based on the operating system with configurable time.sleep(n)"""
    time.sleep(n)
    os.system("cls" if os.name == "nt" else "clear")


class LoadPromo():
    def __init__(self,name,data,validity,price):
        self.name = name
        self.data = data
        self.validity = validity
        self.price = price

class LoadRegistrationApp:
    #Initialze Dictionary to prevent recreating/reinitializing everytime a function is called
    PROMOS = {
        1: (
            LoadPromo("GIGA VIDEO 50","4GB","3 days",50),
            LoadPromo("GIGA VIDEO 99","9GB","7 days",99)
        ),

        2: (
            LoadPromo("GIGA VIDEO+ 50","5GB video + 1GB open access","3 days",50),
            LoadPromo("GIGA VIDEO+ 99","10GB video + 2GB open access","7 days",99)
        ),

        3: (
            LoadPromo("ALL NET 50","2GB open access","3 days",50),
            LoadPromo("ALL NET 99","6GB open access","3 days",99)
        ),

        4: (
            LoadPromo("GIGA STORIES 50","4GB","3 days",50),
            LoadPromo("GIGA STORIES 99","9GB","7 days",99)
        ),

        5: (
            LoadPromo("GIGA GAMES 50","4GB for gaming","3 days",50),
            LoadPromo("GIGA GAMES 99","9GB for gaming","7 days",99)
        )
    }

    MENU_NAMES = {
    1: "GIGA VIDEO",
    2: "GIGA VIDEO+",
    3: "GIGA ALL NET",
    4: "GIGA IG+FB+TikTok",
    5: "GIGA GAMES",
    }
    # LoadRegisterionApp Object Constructor
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.balance = self.get_balance()
        self.selected_promo = None
    # Helper Functions
    @staticmethod
    def get_int(msg:str,error_msg:str=None):
        """
        Helper Function for getting a integer type data variable
        and will handle input data without raising an error and has a dynamic error catching message/feedback

        """
        while True:
            try:
                int_number = int(input(f"{msg} "))
                return int_number
            except ValueError:
                print("Input Must be Integer(1)!" if error_msg == None else f"{error_msg}")
                
    @staticmethod
    def get_float(msg:str,error_msg:str=None):
        """
        Helper Function for getting a float type data variable
        and will handle input data without raising an error and has a dynamic error catching message/feedback
        """
        while True:
            try:
                float_number = float(input(f"{msg} "))
                return float_number
            except ValueError:
                print(f"Input Must be Float(0.0)!" if error_msg == None else f"{error_msg}")
                
    @staticmethod
    def get_str(msg:str):
        """
        Helper Function for getting a string type data variable
        with dynamic messaging
        """
        return input(f"{msg}: ")

    @classmethod
    def get_promos(cls, choice):
        return cls.PROMOS.get(choice)
    
    @staticmethod
    def confirm_exit(msg:str=None):
        """
        Helper Function checking while loop condition at main func
        whether to end or continue to loop
        """
        return input(f"Want to {msg}? Y/N: ").upper() == "Y"


    # Display Functions
    @staticmethod
    def display_ussd_code():
        print("="*26)
        print("Load Services")
        print("="*26)

    @staticmethod
    def display_main_menu():
        print("="*26)
        print("\tMain Menu")
        print("="*26) 

    def user_info(self):
        print(f"User: {self.fname.capitalize()}, {self.lname.capitalize()}")

    def display_balance(self):
        print(f"Balance: ${self.balance:.2f}")

    @staticmethod
    def display_promo_menu(promo1, promo2):
        print("="*26)
        print("\tSelect Load")
        print("="*26)
        print(f"[1] {promo1.name} - ${promo1.price} ")
        print(f"[2] {promo2.name} - ${promo2.price} ")
        print(f"[3] Exit")

    @staticmethod
    def display_promo_detail(promo):
        print("="*26)
        print(f"Promo\t: {promo.name}")
        print(f"Data\t: {promo.data}")
        print(f"Validity: {promo.validity}")
        print(f"Price\t: {promo.price}")
        print("="*26)
        print(f"[1] Buy\n[2] Cancel")



    # Validation Functions
    @staticmethod
    def ussd_session():
        """
        Loops around until correct uusd code is inputted
        if success, fully proceed to the main func
        """
        while True:
            LoadRegistrationApp.display_ussd_code()

            result = LoadRegistrationApp.get_ussd_code()

            if result == "valid":
                print("Valid USSD code!")
                clear_screen()
                break

            elif result == "empty":
                print("USSD can't be empty!")

            else:
                print("Invalid USSD code. Try again.")



    #Input Funcs
    def get_balance(self):
        balance = LoadRegistrationApp.get_float("Enter Balance: $","Enter the Money Bitch!")
        return balance
    
    @staticmethod
    def get_user_info():
        fname = LoadRegistrationApp.get_str("Enter First Name")
        lname = LoadRegistrationApp.get_str("Enter Last Name")
        return fname,lname
    
    @staticmethod
    def get_ussd_code():
        ussd_code = LoadRegistrationApp.get_str("Enter USSD Code (*123#)").strip()

        if not ussd_code:
            return "empty"

        if LoadRegistrationApp.validate_ussd_code(ussd_code):
            return "valid"

        return "invalid"

    #Logics Func
    @staticmethod
    def validate_ussd_code(ussd_code):
        return ussd_code.strip() == "*123#"
    
    def buy_promo(self, promo):
        """
        Get the passed referred object's variable balance to be processed
        returns False after execution
        """
        if self.balance < promo.price:
            return False

        self.balance -= promo.price
        self.selected_promo = promo.name
        return True


    def promo_menus(self, choice):
        promos = self.get_promos(choice)

        if promos is None:
            return None

        self.display_promo_menu(promos[0], promos[1])

        return promos
    
    #Sessions

    def promo_menu_session(self,choice):
        while True:
            promos = self.promo_menus(choice)

            if promos is None:
                print("Invalid promo category.")
                return

            promo_choice = self.get_int("Choice:")

            if promo_choice == 1:
                self.promo_menu_detail_session(promos[0])
                return 

            elif promo_choice == 2:
                self.promo_menu_detail_session(promos[1])
                return 

            elif promo_choice == 3:
                return 
            else:
                print("Invalid choice.")
                clear_screen_delayed(2)

            

    def promo_menu_detail_session(self,promo):
        while True:
            clear_screen()
            self.display_promo_detail(promo)
            confirm = self.get_int("Choice:")
            
            if confirm == 1:
                    if self.buy_promo(promo):
                        print(f"You're now subscribed to {promo.name}!")
                        print(f"Remaining balance: {self.balance:.2f}")
                    else:
                        print("Insufficient Balance!")
                    clear_screen_delayed(2)
                    return   
            elif confirm == 2:
                if self.confirm_exit("Cancel"):
                    break
            else:
                print("Invalid choice.")
                clear_screen_delayed(2)





# Main Function
def main():
    LoadRegistrationApp.ussd_session() 

    fname, lname = LoadRegistrationApp.get_user_info()

    acc1 = LoadRegistrationApp(fname, lname)
    while True:
        clear_screen()
        LoadRegistrationApp.display_main_menu()
        acc1.user_info()
        acc1.display_balance()
        print("-"*26)
        for key, value in LoadRegistrationApp.MENU_NAMES.items():
            print(f"[{key}] {value}")
        print("[6] EXIT")
        choice = LoadRegistrationApp.get_int("Choice:")

        if 1 <= choice <= 5:
            clear_screen()
            acc1.promo_menu_session(choice)
        elif choice == 6:
            clear_screen()
            if LoadRegistrationApp.confirm_exit("Exit"):
                break
        else:
            print("Invalid choice.")
            time.sleep(2)


if __name__ == '__main__':
    clear_screen() 
    main()