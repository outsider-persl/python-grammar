# while [condition=True]:
#     [code block]

loopcount = 10
while loopcount > 0:
    print(loopcount)
    loopcount -= 1


# continue : Skip the rest of the code block and continue with the next iteration
loopcount = 10
while True:
    if loopcount == 0:
        print("Loop ends")
        break
    print(f"Infinite loop,{loopcount}")
    loopcount -= 1
    continue
    print("This will not be printed")


def guess_number():
    number = 10
    while True:
        guess = int(input("Enter a number: "))
        if guess == number:
            print("You guessed it right!")
            break
        if guess < number:
            print("Try a higher number!")
            continue
        if guess > number:
            print("Try a lower number!")
            continue


list_of_numbers = [1, 2, 3, 4, 5]
for index, number in enumerate(list_of_numbers):
    print(index, number)

# for loop with range
students = ["Hermoine", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

# dictionary
students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
# for key in dictionary
for key in students:
    # sep: separator
    print(key, students[key], sep=": ")

NAME = "name"
HOUSE = "house"
PATRONUS = "patronus"
students = [
    {NAME: "Hermoine", HOUSE: "Gryffindor", PATRONUS: "Otter"},
    {NAME: "Harry", HOUSE: "Gryffindor", PATRONUS: "Stag"},
    {NAME: "Ron", HOUSE: "Gryffindor", PATRONUS: "Jack Russell terrier"},
    {NAME: "Draco", HOUSE: "Slytherin", PATRONUS: None},
]

for student in students:
    print(student[NAME], student[HOUSE], student[PATRONUS], sep=", ")
