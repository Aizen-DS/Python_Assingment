Student = {
    "Alice": 85,
    "noel" : 97,
}

name = input("Enter the student's name: ")

if name in Student:
    print(f"{name}'s marks:{Student[name]}")
else:
    print("Student not foundjpn")