# solution for 2023 - day 4
from aoc import aoc

data = aoc.get_input(2023, 4).read_text().splitlines()

MATCHES = [
    len(list(set(w) & set(h)))
    for w, h in [[s.split() for s in line[10:].split(" | ")] for line in data]
]


def ans1() -> int:
    return sum([int(2 ** (m - 1)) for m in MATCHES])


def ans2() -> int:
    copies = [1] * len(MATCHES)

    for i, m in enumerate(MATCHES):
        for a in range(i + 1, i + m + 1):
            copies[a] += copies[i]

    return sum(copies)


if __name__ == "__main__":
    aoc.print_answer(1, ans1())
    aoc.print_answer(2, ans2())
