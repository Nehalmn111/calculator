# calculator.py
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def square(a):
    return a ** 2

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error! Negative number."

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square\n6. Square Root\n7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == "7":
            print("Exiting Calculator. Goodbye!")
            break

        if choice in ["1","2","3","4"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(num1, num2))
            elif choice == "2":
                print("Result:", subtract(num1, num2))
            elif choice == "3":
                print("Result:", multiply(num1, num2))
            elif choice == "4":
                print("Result:", divide(num1, num2))

        elif choice in ["5", "6"]:
            num = float(input("Enter a number: "))
            if choice == "5":
                print("Result:", square(num))
            elif choice == "6":
                print("Result:", square_root(num))
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
