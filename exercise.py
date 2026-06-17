import math
import time
#exercise 1
def circle():
    def get_variables():
        r = float(input("Enter Radius of Circle: "))
        return r
    def calucate_circle_rad(r):
        return 2 * math.pi * r

    def calculate_circle_area(r):
        return math.pi * (r**2)

    def display_result(circumference,area):
        print(f"The Cirumference of a circle with a radius of {r} is equal to: {round(circumference, 2)}cm²")
        print(f"The Cirumference of a circle with a radius of {r} is equal to: {round(area, 2)}cm²")

    r = get_variables()
    circumference = calucate_circle_rad(r)
    area = calculate_circle_area(r)
    display_result(circumference,area)
#exercise 2
def triangle():
    def get_variables():
        a = float(input("Enter A side value: "))
        b = float(input("Enter B side value: "))
        return a,b
    def calculate_area_triangle(a,b):
        return math.sqrt(pow(a,2)+pow(b,2))
    def display_result(a,b,c):
        print(f"The Area of Triangle with side {a}, and side {b} is equal to: {c}")
    
    a,b = get_variables()
    c = calculate_area_triangle(a,b)
    display_result(a,b,c)





# exercise, for user registration input validation and creation validation
def validate_username():
    def get_username():
        username = input("Enter Username: ")
        return username
    def username_validation(username):
        
        if len(username) > 12:
            print("Username cannot exceed 12 Characters!")
        elif not username.find(" ") == -1:
            print("Username Cannot have spaces!")
        elif not username.isdigit():
            print("Username cannot have digits!")
        else: 
            print("Username is Accepted")
    username = get_username()
    username_validation(username)

def validate_password():
    def get_password():
        password=input("Enter Password: ")
        return password
    def password_validation(password):
        specialCharacters = ("@","!","#")
        if len(password) < 8:
            print("Password cannot be less than 8 Characters!")
        elif not password.find(" ") == -1:
            print("Password cannot contain spaces!")
        elif not any(char.isdigit() for char in password):
            print("Password must contain digits!")
        elif not any(char in specialCharacters for char in password):
            print("Password must contain special characters!")
        else:
            print("Password is Validated")
    
    password = get_password()
    password_validation(password)



def countdown_timer():

    def get_time():
        my_time_unit = (input("Enter Time Unit (Months, Weeks, Days, Hours, Minutes, Seconds): "))
        my_time_unit=my_time_unit.capitalize()
        my_time = int(input("Enter time: "))

        time_units = {
            "Seconds": 1,
            "Minutes": 60,
            "Hours": 3600,
            "Days": 86400,
            "Weeks": 604800,
            "Months": 2592000,
        }

        if my_time_unit in time_units:
            return my_time * time_units[my_time_unit]
        else:
            print("Wrong Input")
            countdown_timer()
        


    def timer_logic(my_time):
        
        for x in range(my_time, -1, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600) % 24
            days = int(x / 86400) % 7
            weeks = int(x / 604800) % 4
            months = int(x / 2592000) 
            print(f"Month {months:02} :Week {weeks:02} :Days {days:02} :Hours {hours:02} :Minutes {minutes:02} :Seconds {seconds:02}")
            time.sleep(1)
        print("Time's UP!!!")

    my_time = get_time()
    timer_logic(my_time)


def twodimensional_array():
    groceries = [["Apple","Coconut","Banana"],
                 ["Radish","Potato","Tomato"],
                 ["Chicken","Fish","Turkey"]]

    for row in groceries:
        for col in row:
            print(col, end=" ")
        print()   

twodimensional_array()



