# solution for 2022 - day 3
from aoc import aoc

data = aoc.get_input(2022, 3).read_text().splitlines()


def common(*items: str) -> str:
    sets = [set(item) for item in items]
    return list(set.intersection(*sets)).pop()


def priority(x: str) -> int:
    return ord(x) - (96 if x >= "a" else 38)


group = []
total = group_total = 0

for line in data:
    mid = len(line) // 2
    comp1, comp2 = line[:mid], line[mid:]
    total += priority(common(comp1, comp2))

    group.append(line)
    if len(group) == 3:
        group_total += priority(common(*group))
        group = []


def ans1() -> int:
    return total


def ans2() -> int:
    return group_total


if __name__ == "__main__":
    aoc.print_answer(1, ans1())
    aoc.print_answer(2, ans2())
