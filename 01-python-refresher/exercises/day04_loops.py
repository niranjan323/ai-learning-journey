"""
Day 04 — Loops & Conditionals
-----------------------------
Control the flow of your program: make decisions with `if`,
and repeat work with `for` and `while` loops.

Run this file:
    python day04_loops.py
"""


def main() -> None:
    # 1. Conditionals: if / elif / else
    temperature = 25
    if temperature > 30:
        print("It's hot.")
    elif temperature > 15:
        print("It's pleasant.")
    else:
        print("It's cold.")

    # 2. for loop over a list
    colors = ["red", "green", "blue"]
    for color in colors:
        print("Color:", color)

    # 3. for loop with range()
    for i in range(1, 6):           # 1, 2, 3, 4, 5
        print(f"{i} squared is {i ** 2}")

    # 4. enumerate(): get the index and the value together
    for index, color in enumerate(colors):
        print(f"{index}: {color}")

    # 5. while loop: repeat until a condition becomes False
    countdown = 3
    while countdown > 0:
        print("Countdown:", countdown)
        countdown -= 1
    print("Lift off!")

    # 6. break and continue
    for number in range(1, 11):
        if number == 8:
            break               # stop the loop entirely
        if number % 2 == 0:
            continue            # skip the rest of this iteration
        print("Odd number:", number)


if __name__ == "__main__":
    main()
