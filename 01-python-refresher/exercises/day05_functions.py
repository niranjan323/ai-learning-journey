"""
Day 05 — Functions
-------------------
Functions let you name a block of code and reuse it. They can take
inputs (arguments) and give back outputs (return values).

Run this file:
    python day05_functions.py
"""


# 1. A simple function with no arguments
def greet() -> None:
    print("Hello from a function!")


# 2. A function with arguments and a return value
def add(a: int, b: int) -> int:
    return a + b


# 3. A default argument value
def greet_person(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


# 4. *args: accept any number of positional arguments
def total(*numbers: float) -> float:
    return sum(numbers)


# 5. **kwargs: accept any number of named arguments
def describe(**details: str) -> None:
    for key, value in details.items():
        print(f"  {key}: {value}")


def main() -> None:
    greet()

    result = add(3, 4)
    print("add(3, 4) =", result)

    print(greet_person("Ada"))                       # uses default greeting
    print(greet_person("Grace", greeting="Hi"))      # custom greeting

    print("total(1, 2, 3, 4) =", total(1, 2, 3, 4))

    print("describe(...):")
    describe(name="Ada", role="engineer", language="Python")


if __name__ == "__main__":
    main()
