def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! "
    return x/y

def calculator():
    print("Select operation: ")
    print("1. Add")
    print("2. Subtract ")
    print("3. Multiply ")
    print("4. Divide ")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ['1', '2', '3', '4']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == '1':
                print(f"{a} + {b} = {add(a,b)}")
            elif choice == '2':
                print(f"{a} - {b} = {subtract(a, b)}")
            elif choice == '3':
                print(f"{a} * {b} = {multiply(a, b)}")
            elif choice == '4':
                print(f"{a}/ {b} = {divide(a, b)}")

            next_calculation = input("Do you want calculations? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

calculator()


