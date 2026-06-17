from car import Car
import time
"""
class vowelCounter:
    def vowelCounter(word, vowels, upper_vowels):
        vowel_count=0

        for i in range(len(word)):
            if word[i] in vowels or word[i] in upper_vowels:
                vowel_count+=1
        print("Total Vowel in ",word,"is: ", vowel_count)  

    def initVowelList():
        vowels=['a','e','i','o','u']
        upper_vowels=[x.upper() for x in vowels]
        return vowels,upper_vowels

    word=input("Enter a Word: ")
    vowels,upper_vowels=initVowelList()
    vowelCounter(word,vowels,upper_vowels)

"""
"""
class currencyExchange:

    def exchange_money(budget, exchangeRate):
        return budget/exchangeRate
    
    def get_change(budget, exchangingValue):
        return budget-exchangingValue
    
    def get_value_of_bills(denomination, numberOfBills):
        return numberOfBills * denomination
    
    def get_number_of_bills(amount, denomination):
        return amount // denomination

    def get_leftover_of_bills(amount, denomination):
        return amount % denomination

    def exchangeable_value(budget, exchangeRate, spread, denomination):
        spreadDecimal=spread/100
        actualRate=exchangeRate * (1+spreadDecimal)
        rawValue=budget/actualRate
        exchangeableValue=int((rawValue// denomination) * denomination)
        return exchangeableValue

    def initializeInput():
        budget=float(input("enter budget: "))
        exchangeRate=float(input("enter exchange rate: "))
        exchangingValue=float(input("Enter your Exchanging Value: "))
        denomination=float(input("Enter your denomination: "))
        numberOfBills=int(input("Enter your Bills: "))
        amount=float(input("Enter amount: "))
        spread=int(input("Enter Spread value: "))
        return budget, exchangeRate, exchangingValue, denomination, numberOfBills, amount, spread
    def choices():
        print("1. exchange_money")
        print("2. get_change")
        print("3. get_value_of_bills")
        print("4. get_number_of_bills")
        print("5. get_leftover_of_bills")
        print("6. exchangeable_value")
        choice=int(input("Enter your choice: "))
        return choice
    
    choice=choices()
    budget, exchangeRate, exchangingValue, denomination, numberOfBills, amount, spread = initializeInput(choices)


    totalExchangeMoney=exchange_money(budget,exchangeRate)
    totalChange=get_change(budget, exchangingValue)
    totalValueofBill=get_value_of_bills(denomination, numberOfBills)
    totalNumberOfBills=get_number_of_bills(amount,denomination)
    totalExchangeableValue=exchangeable_value(budget, exchangeRate, spread, denomination)
    print("Total Echangeable Value is: ",totalExchangeableValue)
"""
"""
car1=Car("Duesenberg", "Model J", 1938, False)
car1.honk()
time.sleep(5)

car2=Car("Corvette","C6",2005, True)
car2.honk()
input("Enter to Exit...")
"""
my_list = ['a','a','a']

if len(set(my_list)) == 1:
    print("TRUE")
else:
    print("FAlse")