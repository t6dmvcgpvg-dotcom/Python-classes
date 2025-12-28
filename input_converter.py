# Program to read user input and convert strings to float
# Demonstrates use of input() and float() functions

# Read first number from user
user_input1 = input("Enter first number: ")
number1 = float(user_input1)

# Read second number from user
user_input2 = input("Enter second number: ")
number2 = float(user_input2)

# Calculate total without using sum() function or 'sum' variable name
total = number1 + number2

# Display the result
print("First number:", number1)
print("Second number:", number2)
print("Total:", total)
