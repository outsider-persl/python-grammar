try:
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

# fileio exceptions
try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("file.txt not found")
except PermissionError:
    print("You don't have permission to read file.txt")
except Exception as e:
    print(f"An error occurred: {e}")

# raise keyword: used to throw an exception
# raise ValueError("An error occurred")

