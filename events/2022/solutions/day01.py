# solution for 2022 - day 1
from aoc import aoc

inp = aoc.get_input(2022, 1)

inventory = inp.read_text().split("\n\n")
inventory = [tuple(map(int, items.split())) for items in inventory]

inventory.sort(key=sum, reverse=True)


def ans1() -> int:
    return sum(inventory[0])


def ans2() -> int:
    return sum(map(sum, inventory[:3]))


if __name__ == "__main__":
    aoc.print_answer(1, ans1())
    aoc.print_answer(2, ans2())
