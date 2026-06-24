"""
Day 02 — Core Data Types
------------------------
Python's most common built-in types: int, float, str, and bool.
This file shows how to create them, convert between them, and use
basic operations.

Run this file:
    python day02_datatypes.py
"""


def main() -> None:
    # 1. Numbers: integers and floats
    count = 10            # int
    price = 19.99         # float
    print("count + 5 =", count + 5)
    print("price * 2 =", price * 2)
    print("10 / 3 =", 10 / 3)      # true division -> float
    print("10 // 3 =", 10 // 3)    # floor division -> int
    print("10 % 3 =", 10 % 3)      # remainder (modulo)
    print("2 ** 8 =", 2 ** 8)      # exponent

    # 2. Strings: text
    greeting = "Hello"
    target = "World"
    print(greeting + ", " + target + "!")   # concatenation
    print(greeting * 3)                       # repetition
    print(len(greeting))                      # length
    print(greeting.upper(), greeting.lower())
    print("World" in "Hello World")           # substring check -> True

    # 3. Booleans: True / False
    is_active = True
    is_admin = False
    print("AND:", is_active and is_admin)
    print("OR :", is_active or is_admin)
    print("NOT:", not is_active)

    # 4. Type conversion (casting)
    number_text = "42"
    number = int(number_text)     # str -> int
    print(number + 8)             # 50
    print(str(number) + "!")      # int -> str -> "42!"
    print(float(number))          # 42.0

    # 5. Checking a type
    print(type(price))            # <class 'float'>
    print(isinstance(count, int)) # True


if __name__ == "__main__":
    main()
