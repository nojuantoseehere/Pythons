# exercise 5 topic while loop

def get_value():
    principal = float(input("Enter your Principal Amount: "))
    int_rate = float(input("Enter the interest rate: "))
    time_compound = int(input("Enter interest compound: "))
    time_period = int(input("Enter the time period(Years): "))
    return principal, int_rate, time_compound, time_period
    
def compound_interest_logic(principal, int_rate, time_compound, time_period):
    i = 0

    while i <= time_period:
        amount = principal*(1 + int_rate/time_compound)**(time_compound*i)
        print(f"The amount for time period {i} is equal to {round(amount,2)}")
        i +=1
        
    interest = amount - principal
    print(f"The final amount is {round(amount,2)}")
    print(f"Interest earned is {round(interest,2)}")
    
principal, int_rate, time_compound, time_period= get_value()
compound_interest_logic(principal, int_rate, time_compound, time_period)