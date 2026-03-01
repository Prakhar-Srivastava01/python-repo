# ============================
# Advanced Calculator (CLI)
# Author: Prakhar Srivastava
# ==============================

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

def calculator():
    print("\n===== Python Calculator =====")

    while True:
        print("""
Choose Operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Power (^)
6. Exit
""")

        choice = input("Enter choice (1-6): ")

        if choice == "6":
            print("Calculator Closed ✅")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice! Try again.\n")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers!\n")
            continue

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        elif choice == "5":
            result = power(num1, num2)

        print(f"\nResult: {result}\n")


# Run program
if __name__ == "__main__":
    calculator()
