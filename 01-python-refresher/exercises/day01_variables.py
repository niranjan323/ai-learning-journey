"""
Day 01 — Variables & Basic Input/Output
----------------------------------------
A variable is a name that points to a value. Python figures out the type
automatically, so you don't need to declare it.

Run this file:
    python day01_variables.py
"""


def main() -> None:
    # 1. Assigning variables
    name = "Ada"          # a string (text)
    age = 36              # an integer (whole number)
    height_m = 1.70       # a float (decimal number)
    is_engineer = True    # a boolean (True/False)

    # 2. Printing values
    print("Name:", name)
    print("Age:", age)
    print("Height (m):", height_m)
    print("Is engineer?", is_engineer)

    # 3. f-strings: the cleanest way to build text from variables
    print(f"{name} is {age} years old and {height_m} m tall.")

    # 4. Variables can be reassigned (and even change type)
    age = age + 1
    print(f"Next year {name} will be {age}.")

    # 5. Reading input from the user (input always returns a string)
    #    Uncomment the lines below to try it interactively:
    # user_name = input("What is your name? ")
    # print(f"Hello, {user_name}!")

    # 6. Multiple assignment
    x, y, z = 1, 2, 3
    print("x, y, z =", x, y, z)


if __name__ == "__main__":
    main()
