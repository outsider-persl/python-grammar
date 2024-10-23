def basic(x, y):
    if x > y:
        return "x is greater than y"
    elif x < y:
        return "x is less than y"
    else:
        return "x is equal to y"


def and_f(x, y):
    if x > 10 and y > 10:
        return "Both x and y are greater than 10"
    else:
        return "Either x or y is less than or equal to 10"


def or_f(x, y, z):
    if x > 10 or y > 10:
        return "Either x or y is greater than 10"
    if x < y < z:
        return "<<<<<"
    if x > y > z:
        return ">>>>>"
    else:
        return "Both x and y are less than or equal to 10"


def is_even(n):
    return True if n % 2 == 0 else False


def main():
    print(basic(10, 20))
    print(and_f(10, 20))

    print(or_f(3, 2, 1))
    print(or_f(10, 20, 30))

    print(is_even(10))


main()
