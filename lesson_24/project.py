def add(a, b):
    return a + b

def subtract(a, b):
    return(a - b)

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    print("===Function Calculator===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose an operation (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid operation choice!")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number:"))

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")

        elif choice == '4':
            try:
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            except ZeroDivisionError:
                print("Errpr: Cannot divide by zero!")

    except ValueError:
        print("Error: Invalid input! Please enter numbers only.")

calculator()