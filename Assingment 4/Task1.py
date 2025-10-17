try:
    with open('sample.txt','r') as file:
        for line_number, line in enumerate(file, start=1):
            print(f"line {line_number}:{line.strip()}")

except FileNotFoundError:
    print("error: the file 'sample.txt' was not found")