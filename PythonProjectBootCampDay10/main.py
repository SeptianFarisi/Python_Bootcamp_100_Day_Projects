import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(art.logo)
    calculate = True
    number1 = int(input(""))

    while calculate:

        ope = input("Operation?\n")
        number2 = int(input(""))

        result = operation[ope](number1, number2)
        print(result)

        ask = input("Want to operation again? type 'y' to continue, "
                    "type 'c' to clear, type 'n' to exit\n").lower()

        if ask == "y":
            number1 = result
        elif ask == "c":
            calculate = False
            calculator()
        else:
            calculate = False

calculator()