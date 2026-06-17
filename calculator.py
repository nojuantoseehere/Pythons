import time
def addition(a, b):
    total = a + b
    arithmetic_type = "addition"
    return total, arithmetic_type

def subtraction(a, b):
    total = a - b
    arithmetic_type = "subtraction"
    return total, arithmetic_type

def multiplication(a, b):
    total = a * b
    arithmetic_type = "multiplication"
    return total, arithmetic_type

def division(a, b):
    total = a / b
    arithmetic_type="division"
    return total, arithmetic_type
   

def get_variables():
    a = int(input("Enter Variable A: "))
    b = int(input("Enter Variable B: "))
    return a, b

def display_total(total, arithmetic_type, a , b):

    if arithmetic_type in messages:

        operationName = messages[arithmetic_type]
        print(f"The {operationName} of Variable {a}, and Variable {b} is equal to: {total}")
        time.sleep(2)

def choice_logic(choice):

    if choice == 5:
        print("Exiting")
        return False
    
    if choice in operations:
        a, b = get_variables()
        arithmeticOperations=operations[choice]
        total, arithmetic_type = arithmeticOperations(a, b)
        display_total(total, arithmetic_type, a ,b)
    else:
        print("Invalid Command")

    return True

def display_choice():
    print("------------------")
    print("--- CALCULATOR ---")
    print("--- [1] for Addition ---")
    print("--- [2] for Subtraction ---")
    print("--- [3] for Multiplication ---")
    print("--- [4] for Division ---")
    print("--- [5] for Exit ---")

def main():
    is_use = True
    while is_use:
        display_choice()
        choice=int(input("Enter Command Choice: "))
        is_use=choice_logic(choice)

messages={
    "addition":"Sum",
    "subtraction":"Difference",
    "multiplication":"Product",
    "division":"Quotient",
    }
operations = {
    1:addition,
    2:subtraction,
    3:multiplication,
    4:division,
    }

main()
