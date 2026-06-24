import os
import time
import json

#Utility Func
def clear_screen():
    """Clears the console screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")

def clear_screen_delayed(n:int):
    """Clears the console screen based on the operating system with configurable time.sleep(n)"""
    time.sleep(n)
    os.system("cls" if os.name == "nt" else "clear")

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

def get_str(msg:str) -> str:
    """
    Helper Function for getting a string type data variable
    with dynamic messaging
    """
    return input(f"{msg} ")

def write_json(file_path:str,content:dict,file_name:str = None,feedback:bool = None)-> None:
    """
    Helper Function for writing a json file
    """

    try:
        with open(file_path,"w") as file:
            json.dump(content,file, indent=4)
            if feedback:
                print(f"File {file_name} Successfully Save")
    except OSError:
        print(f"Saving {file_name} Failed! Please Try Again!")


def load_json(file_path:str,file_name:str = None)-> dict:
    """
    Helper Function for reading/loading a json file
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Loading {file_name} Failed! Please Try Again!")
        return {}