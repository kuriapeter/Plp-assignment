# Simple Calculator Program
print("Simple Calculator")
print("Operations: + (Addition), - (Subtraction), * (Multiplication), / (Division)")

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation based on operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = "Error! Division by zero."
    else:
        result = num1 / num2
else:
    result = "Invalid operation!"

# Print the result
print(f"Result: {result}")