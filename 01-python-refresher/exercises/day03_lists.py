"""
Day 03 — Collections: Lists, Tuples, Dicts, Sets
------------------------------------------------
Collections let you store many values in one variable.

Run this file:
    python day03_lists.py
"""


def main() -> None:
    # 1. Lists: ordered and changeable (mutable)
    fruits = ["apple", "banana", "cherry"]
    print("List:", fruits)
    print("First item:", fruits[0])     # indexing starts at 0
    print("Last item:", fruits[-1])     # negative index counts from the end

    fruits.append("date")               # add to the end
    fruits[1] = "blueberry"             # change an item
    fruits.remove("apple")              # remove by value
    print("Updated list:", fruits)
    print("Slice [0:2]:", fruits[0:2])  # first two items

    # 2. List comprehension: build a list in one line
    squares = [n * n for n in range(1, 6)]
    print("Squares:", squares)          # [1, 4, 9, 16, 25]

    # 3. Tuples: ordered but unchangeable (immutable)
    point = (10, 20)
    print("Tuple:", point, "-> x =", point[0])

    # 4. Dictionaries: key/value pairs
    person = {"name": "Ada", "age": 36}
    print("Name:", person["name"])
    person["job"] = "engineer"          # add a new key
    print("Keys:", list(person.keys()))
    print("Values:", list(person.values()))
    for key, value in person.items():
        print(f"  {key} -> {value}")

    # 5. Sets: unordered collection of unique items
    numbers = {1, 2, 2, 3, 3, 3}
    print("Set (duplicates removed):", numbers)
    print("Union:", {1, 2} | {2, 3})
    print("Intersection:", {1, 2} & {2, 3})


if __name__ == "__main__":
    main()
