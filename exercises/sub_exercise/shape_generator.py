
def get_size():
    numb_row = input("Enter number of Row: ")
    numb_col = input("Enter number of Col: ")
    return int(numb_row),int(numb_col)

def get_symbol():
    symbol = input("Enter symbol for shape: ")
    return symbol

def get_shape():
    shapeChoice = input("Enter your choosen shape: ").capitalize()
    return shapeChoice

def display_shape_logic(shapeChoice):
    if shapeChoice == "Square":
        return display_square(numb_row,numb_col,symbol)
    elif shapeChoice == "Triangle":
        return display_triangle(numb_row,symbol)


def display_square(numb_row,numb_col,symbol):
    for row in range(numb_row):
        for col in range(numb_col):
            print(f"{symbol}", end="")
        print()

def display_triangle(numb_row,symbol):
    for row in range(numb_row):
        print(" " * (numb_row - row - 1), end="")

        for col in range(2 * row + 1):
            print(symbol, end="")

        print()


numb_row, numb_col =get_size()
symbol=get_symbol()
shapeChoice = get_shape()
display_shape_logic(shapeChoice)

