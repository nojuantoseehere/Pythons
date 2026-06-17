def get_number(msg:str):
    while True:
        try:
            number = int(input(f"Enter Number for {msg} : "))
            return number
        except ValueError:
            print("Invalid Input")

def get_word(msg:str):
    while True:
        try:
            word = input(f"Enter Word for {msg} : ")
            return word
        except ValueError:
            print("Invalid Input")

#No.1 Exercise Even or Odd
def is_odd_or_even(number):
    if number % 2 == 0:
        print(f"{number} is an Even Number")
    else:
        print(f"{number} is an Odd Number")

number = get_number("odd or even")
is_odd_or_even(number)

#No.2 Exercise Vowel Counter
def vowel_counter(words):
    vowels = ['a','e','i','o','u']
    upper_vowels = [x.upper() for x in vowels]
    vowel_count = 0
    for word in words:
        if word in vowels or word in upper_vowels:
            vowel_count += 1
    print(f"There are {vowel_count} vowel/s in {words}")        

words = get_word("vowel counter")
vowel_counter(words)

#No.3 Exercise Multiplication Table
def multiplication_table(multiplication_number):
    for i in range(1,11):
       table = multiplication_number * i
       print(f"{multiplication_number} * {i} = {table}")
multiplication_number = get_number("multiplication table")
multiplication_table(multiplication_number)


#No.4 Exercise number guess
import random
def number_randomizer():
    randomize_number = random.randint(1,100)
    return randomize_number

def number_guess_logic(numb_guess,randomize_numb):
    

    if numb_guess > randomize_numb:
        return "too_high", True
    elif numb_guess < randomize_numb:
        return "too_low", True
    
    return "guessed", False

def number_guess_feedback(feedback):
    feedback_msg = {
        "too_high":"too high",
        "too_low":"too low!",
        "guessed":"correct!"
    }
    print(f"Your guess number is {feedback_msg[feedback]}")

is_running = True
randomize_numb = number_randomizer()
while is_running:
    numb_guess = get_number("to guess number")
    result,status = number_guess_logic(numb_guess,randomize_numb)
    number_guess_feedback(result)
    is_running = status

#No.4 Password strength checker
def password_validation(password):

    if len(password) < 8:
        print("Password must be equal or greater than 8 characters")
        return False
    elif not any(char.isdigit() for char in password):
        print("Password must contain digits!")
        return False
    elif not any(char.isupper() for char in  password):
        print("Password must contain Upper Case Letter")
        return False
    elif not any(char.islower() for char in  password):
        print("Password must contain Lower Case Letter")
        return False
    else:
        return True

def password_checker(is_strength):
    if is_strength: 
        print("Password is Strong")
        return False
    else:
        print("Password is Weak")
        return True

is_running_password = True

while is_running_password:
    password = input("Enter password to check: ")
    is_strength = password_validation(password)
    is_running_password = password_checker(is_strength)


