# Function to perform basic arithmetic operations
def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:  # Prevent division by zero
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation."

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Perform the calculation and display the result
result = calculator(num1, num2, operation)
print(f"The result of {num1} {operation} {num2} is: {result}")
