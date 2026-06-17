# Create a Concession Stand Program (Dictionary)
# Topic Applied if-else, while, for loop and data collection

def display_menu(menu):
    for key, value in menu.items():
        print(f"Item: {key:10}: Price: ${value:.2f}")

def get_menu(cart, menu):
    add_cart = str(input("Add to Cart: ").lower())   
    if add_cart in menu.keys():
        cart.append(add_cart)
    else:
        print("Sorry the item doesnt exist at the menu!")
        get_menu()
    return cart

def display_cart_items(cart):
    i = 0 
    print("Your items at your cart")
    for item in cart:
        print(f"Item no.{i+1} {item}")
        i+=1

def continue_add_cart():
    choice = input("Continue adding menu to cart? (Y/N) ").upper()
    if choice =="Y":
        return True
    elif choice == "N":
        return False
    else: 
        continue_add_cart()

def calculate_total_price(cart, menu,total):
    
    for item in cart:
        if item in menu:
            total += menu.get(item)
    return total
def display_total(total):
    print(f"Total Cost: ${total:.2f}")




menu = {
    "pizza" : 3.00,
    "popcorn" : 4.50,
    "fries" : 6.00,
    "chips" : 2.50,
    "pretzel" : 1.00,
    "soda" : 3.50,
    "lemonade" : 4.25 
}

cart = []
total = 0
is_add_cart = True

print("=== Menu ===")
display_menu(menu)

while is_add_cart:
    cart = get_menu(cart, menu)
    print()
    display_cart_items(cart)
    print()
    is_add_cart = continue_add_cart()
    print()
total = calculate_total_price(cart, menu,total)
display_total(total)