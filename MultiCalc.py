import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "Error! Cannot compute the square root of a negative number."
    return math.sqrt(a)

def logarithm(a, base=math.e):
    if a <= 0:
        return "Error! Logarithm of non-positive numbers is undefined."
    return math.log(a, base)

def factorial(a):
    if not a.is_integer() or a < 0:
        return "Error! Factorial is not defined for non-integers or negative numbers."
    return math.factorial(int(a))

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

def calculator():
    print("Welcome to the Multipurpose Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Factorial")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")

    while True:
        choice = input("Enter choice (1-11): ")

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
            elif choice == '5':
                print(f"The result is: {power(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter number: "))
            print(f"The result is: {sqrt(num)}")

        elif choice == '7':
            num = float(input("Enter number: "))
            base = input("Enter base (default is e): ")
            if base == "":
                print(f"The result is: {logarithm(num)}")
            else:
                print(f"The result is: {logarithm(num, float(base))}")

        elif choice == '8':
            num = float(input("Enter number: "))
            print(f"The result is: {factorial(num)}")

        elif choice == '9':
            angle = float(input("Enter angle in degrees: "))
            print(f"The result is: {sin(angle)}")

        elif choice == '10':
            angle = float(input("Enter angle in degrees: "))
            print(f"The result is: {cos(angle)}")

        elif choice == '11':
            angle = float(input("Enter angle in degrees: "))
            print(f"The result is: {tan(angle)}")

        else:
            print("Invalid input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

    print("Thank you for using the Multipurpose Calculator!")

# Run the calculator
calculator()
