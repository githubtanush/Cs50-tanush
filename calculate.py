# Get user input for the two numbers
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

# Get user input for the operation to be performed
operation = input("Enter an operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Invalid operation")

# Print the result
print("Result: ", result)
