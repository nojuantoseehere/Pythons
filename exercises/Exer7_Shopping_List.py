def add_item(items):
    item = input("Add item to your shopping list: ")
    items.append(item)


def add_price(prices):
    while True:
        try:
            price = float(input("Enter the price of your item: $"))
            prices.append(price)
            break
        except ValueError:
            print("Please enter a valid number.")


def continue_shopping():
    return input("Continue shopping? (Y/N): ").upper() == "Y"


def display_shopping_list(items, prices):
    print("\n--- Shopping List ---")
    for item, price in zip(items, prices):
        print(f"Item: {item} | Price: ${price:.2f}")


def display_total(prices):
    total = sum(prices)
    print(f"\nTotal Cost: ${total:.2f}")


def shopping_cart_list():
    items = []
    prices = []

    while True:
        add_item(items)
        add_price(prices)

        if not continue_shopping():
            break

    display_shopping_list(items, prices)
    display_total(prices)


shopping_cart_list()