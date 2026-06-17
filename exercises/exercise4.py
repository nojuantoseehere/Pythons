# exercise 4 temp converter if-else topic


def get_temp_unit():
    unit = input("Enter temperature unit (C/F): ")
    return unit
    
def get_temp_val():
    tempValue = float(input("Enter Temperature: "))
    return tempValue
    
def temp_converter_logic(unit, tempValue):

    if unit == "C":
        cel = (tempValue - 32) / 1.8
        print(f"The {round(tempValue,2)}°F is {cel}°C")
    elif unit == "F":
        fahr = (tempValue * 1.8) + 32
        print(f"The {round(tempValue,2)}°C is {fahr}°F")
    else:
        print("Invalid Command.")

unit = get_temp_unit()
tempValue = get_temp_val()
temp_converter_logic(unit, tempValue)