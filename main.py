def greet(name):
    return f"Hello, {name}! Welcome to the Pair Extraordinaire challenge."

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"The sum of {x} and {y} is {add_numbers(x, y)}")
