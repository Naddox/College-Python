# Get user input for variables x and y
x = float(input("Enter the first number (x): "))
y = float(input("Enter the second number (y): "))

# Get user input for the arithmetic operator
operator = input("Enter the arithmetic operator (+, -, *, /): ")

# Perform the arithmetic operation based on the user's input
if operator == '+':
    result = x + y
elif operator == '-':
    result = x - y
elif operator == '*':
    result = x * y
elif operator == '/':
    while y == 0:  # Check for division by zero
        print("Error: Division by zero is not allowed.")
        y = float(input("Enter the second number (y): "))
    result = x / y
else:
    print("Error: Invalid operator entered.")
    exit()

# Print the result
print("Result: " + str(result))