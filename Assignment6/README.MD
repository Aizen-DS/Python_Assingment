# Python Tasks  

This project contains simple Python programs demonstrating **file handling** and **list slicing**.  

---

## Task 1: File Handling  

### Problem Statement  
Write a Python program that:  
1. Creates a file named `sample.txt`.  
2. Writes a number into the file.  
3. Reads the content of the file.  
4. Prints the content.  

### Code Example  
```python
# Task 1: File Handling

# Writing data to the file
with open("sample.txt", "w") as file:
    file.write("5")

# Reading data from the file
with open("sample.txt", "r") as file:
    content = file.read()

# Display the content
print("File Content:", content)

 
# Task 2: List Slicing

# Create a list from 1 to 10
numbers = list(range(1, 11))

# Extract the first five elements
extracted = numbers[:5]

# Reverse the extracted list
reversed_list = extracted[::-1]

# Print lists
print("Original List:", numbers)
print("Extracted List:", extracted)
print("Reversed List:", reversed_list)
