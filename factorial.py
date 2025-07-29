import math

def calculate_factorial():
    print("Welcome to the Factorial Calculator!")
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {num} is {math.factorial(num)}")
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    calculate_factorial()
