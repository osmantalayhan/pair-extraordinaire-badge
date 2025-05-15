def greet(name):
    return f"Hello, {name}! Welcome to the Pair Extraordinaire challenge."

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        print(f"The sum of {x} and {y} is {add_numbers(x, y)}")
        print(f"The product of {x} and {y} is {multiply_numbers(x, y)}")
        print(f"The division of {x} by {y} is {divide_numbers(x, y)}")
        
    except ValueError:
        print("Invalid input! Please enter numeric values.")
