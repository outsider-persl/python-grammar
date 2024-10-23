# '#' is used to comment a line
# this is a comment

# indentation is important in python
print("Hello, World!")

# input("Press Enter to continue...")
# print("Goodbye, World!")

# name = input("What is your name? \n")
# print("Hello, " + name + "!")

# Ask the user for their name
# name = input("What's your name? ")

# The print function automatically includes a piece of code end='\n'
# we can change this to end='' to prevent the print function from adding a new line
# print("hello,", end="")
# print(name)

# we can also use the escape character '\' to escape special characters
# print('hello, "friend"')

# Formatting Strings
# print(f"before, {name}","after")
# name = name.strip()  # remove leading and trailing whitespaces
# print(f"before, {name}","after")

# title = "outsider"
# title = title.title()  # capitalize the first letter of each word
# print(title)

# x = input("What's x? ")
# y = input("What's y? ")

# int(x) converts x to an integer,
# Otherwise, x is a string because input() always returns a string
# z = int(x) + int(y)

# print(z)

# if the user enters a float, the program will crash because int() cannot convert a float to an integer
# number = float(input("Enter a number: "))

# number = int(input("Enter a number: "))
# number = int(number)
# print("The number is", number)

# Get the user's input
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# # Create a rounded result
# z = round(x + y)

# # Print the formatted result
# print(f"{z:,}")

# round() function 4舍6入5取偶
# round(number, ndigits) ;round half to even
# print(round(0.5))
# print(round(7.5))
# print(round(8.5))

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = x / y

# Print the result
print(f"{z:.2f}")

large = 231.8213
large = f"{large:.3f}"
print(large)
