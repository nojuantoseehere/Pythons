#exercise 3 weight converter if-else topic

def get_weight():
    weight = float(input("Enter your Weight: "))
    return weight
def get_unit_choice():
    unit=input("Enter type of weight conversion ('kg','lb'): ")
    return unit
def weight_calculation(weight,unit):
    if unit == "kg":
        converted_weight = weight /  2.205
        units = "kg"
        print(f"Your weight {weight} lb is equivalent to {round(converted_weight,2)} in {units}.")
    elif unit == "lb":
        converted_weight = weight * 2.205
        units = "lb"
        print(f"Your weight {weight} kg is equivalent to {round(converted_weight,2)} in {units}.")
    else:
        print("Invalid User Command.")
        
        

weight = get_weight()
unit = get_unit_choice()
weight_calculation(weight,unit)