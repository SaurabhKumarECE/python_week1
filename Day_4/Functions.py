# 1. Factorial Function
def factorial(n: int) -> int:
    """Returns factorial of a number"""
    if n < 0:
        return -1  # invalid case
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



# 2. Palindrome Checker
def is_palindrome(value: str) -> bool:
    """Checks if a string is palindrome"""
    value = value.lower()  # case insensitive
    return value == value[::-1]  # slicing



# 3. Calculator using Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b



# 4. Lambda Square Function
square = lambda x: x ** 2



# 5. Average of List Function
def average(numbers: list) -> float:
    """Returns average of list elements"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


# Main Execution (Testing all functions)

if __name__ == "__main__":

    # 1. Factorial
    print("---- Factorial ----")
    n = int(input("Enter a number: "))
    print("Factorial:", factorial(n))

    # 2. Palindrome
    print("\n---- Palindrome ----")
    text = input("Enter a string: ")
    print("Palindrome" if is_palindrome(text) else "Not Palindrome")

    # 3. Calculator
    print("\n---- Calculator ----")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Add:", add(a, b))
    print("Subtract:", subtract(a, b))
    print("Multiply:", multiply(a, b))
    print("Divide:", divide(a, b))

    # 4. Lambda Square
    print("\n---- Lambda Square ----")
    num = int(input("Enter a number: "))
    print("Square:", square(num))

    # 5. Average of List
    print("\n---- Average of List ----")
    numbers = list(map(int, input("Enter numbers: ").split()))
    print("Average:", average(numbers))