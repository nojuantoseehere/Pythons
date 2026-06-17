import time

def get_time():
    while True:
        try:
            my_time = int(input("Enter Time: "))
            return my_time
        except ValueError:
            print("Invalid Input!")

def get_time_unit():
    while True:
        try:
            time_unit = str(input("Choose time unit (Seconds/Minutes/Hours/Days): ")).capitalize()
            return time_unit
        except ValueError: 
            print("Invalid Input")

def time_converter(my_time,time_unit):
    
    time_units = {
        "Seconds":1,
        "Minutes":60,
        "Hours":3600,
        "Days":86400
    }

    if time_unit in time_units:
        converted_time = my_time * time_units[time_unit]
        return converted_time
    else:
        print("Invalid Choice!")     


    pass
def count_down_time_logic(converted_time):
    
    for x in range(converted_time,-1,-1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600) % 24
        days = int(x / 86400) % 7
        print(f"{days:02} Days: {hours:02} Hours: {minutes:02} Minutes: {seconds:02} Seconds")
        time.sleep(1)
    print("Time's Up!")

def main():
    my_time = get_time()
    time_unit = get_time_unit()
    converted_time = time_converter(my_time,time_unit)
    count_down_time_logic(converted_time)



if __name__ == '__main__':
    main()