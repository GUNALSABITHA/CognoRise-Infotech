def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

while True:
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Display operation choices
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")
    
    # Get user operation choice
    choice = input("Enter choice (0-4): ")
    
    if choice == '0':
        print("Exiting the calculator. Goodbye!")
        break

    # Perform calculation based on user's choice
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    else:
        print("Invalid input. Please enter a valid operation (0-4).")
        continue

    # result display
    print(f"Result: {result}\n")
#End of the code
