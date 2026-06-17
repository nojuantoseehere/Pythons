#exercise 2 with if-else topic
#create a primitive calculator
def get_operator():
    operator=input("Enter Operator Command ('+','-','*','/'): ")
    return operator

def get_variable():
    a = float(input("Enter A variable: "))
    b = float(input("Enter B variable: "))
    return a,b

def operator_logic(operator,a,b):
        
    if operator == "+":
        result = a + b
        print(f"The sum of var {a} and var {b} is equal to: {round(result)}")
    elif operator == "-":
        result = a - b
        print(f"The difference of var {a} and var {b} is equal to: {round(result)}")
    elif operator == "*":
        result = a * b
        print(f"The product of var {a} and var {b} is equal to: {round(result)}")
    elif operator == "/":
        result = a / b
        print(f"The quotient of var {a} and var {b} is equal to: {round(result)}")
    else:
        print("Invalid Operator Command.")


operator = get_operator()
a, b = get_variable()
operator_logic(operator, a, b)