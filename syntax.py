# '#' is used to comment a line
# this is a comment

# indentation is important in python
print("Hello, World!")

# input("Press Enter to continue...")
# print("Goodbye, World!")

name = input("What is your name? \n")
print("Hello, " + name + "!")

# Ask the user for their name
name = input("What's your name? ")

# The print function automatically includes a piece of code end='\n'
# we can change this to end='' to prevent the print function from adding a new line
print("hello,", end="")
print(name)

# we can also use the escape character '\' to escape special characters
print('hello, "friend"')

# Formatting Strings
name = name.strip()  # removes leading and trailing whitespaces
print(f"hello, {name}")
