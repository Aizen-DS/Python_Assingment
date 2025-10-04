# Task 1: Perform Basic Mathematical Operations

# Taking input from the user 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division carefully (cannot divide by 0)
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"
 
# Display results
print("\n--- Results ---")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")




