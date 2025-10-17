# Task 2: Write and Append Data to a File

# Step 1: Take user input and write it to the file
user_input = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:  
    file.write(user_input + "\n")

print("Data successfully written to output.txt.")

# Step 2: Append additional data
append_input = input("Enter additional text to append: ")

with open("output.txt", "a") as file:  
    file.write(append_input + "\n")

print("Data successfully appended.")

# Step 3: Read and display final content
with open("output.txt", "r") as file:  
    content = file.read()

print("\nFinal content of output.txt:\n")
print(content)
