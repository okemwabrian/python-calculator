import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))  # Convert degrees to radians

def cos(x):
    return math.cos(math.radians(x))  # Convert degrees to radians

def tan(x):
    return math.tan(math.radians(x))  # Convert degrees to radians

def calculator():
    print("Simple Python Calculator")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    
    while True:
        choice = input("\nSelect operation (1-9) or 'q' to quit: ")
        
        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '5', '7', '8', '9']:
            num1 = float(input("Enter first number: "))
            
            if choice in ['1', '2', '3', '4', '5']:  # For basic operations
                num2 = float(input("Enter second number: "))
                
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
                
            elif choice == '5':
                print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
                
            elif choice == '7':
                print(f"Result: sin({num1}) = {sin(num1)}")
                
            elif choice == '8':
                print(f"Result: cos({num1}) = {cos(num1)}")
                
            elif choice == '9':
                print(f"Result: tan({num1}) = {tan(num1)}")
                
        elif choice == '6':  # For square root
            num = float(input("Enter number: "))
            print(f"Result: √{num} = {sqrt(num)}")
            
        else:
            print("Invalid input. Please choose a valid option.")

# Run the calculator
if __name__ == "__main__":
    calculator()
