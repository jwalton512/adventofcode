# solution for 2023 - day 3
import re
from collections import defaultdict
from math import prod

from aoc import aoc

data = aoc.get_input(2023, 3).read_text().splitlines()

NOT_SYMBOLS = "0123456789."

adj = defaultdict(list)

for i, row in enumerate(data):
    above = data[i - 1] if i > 0 else []
    below = data[i + 1] if i < len(data) - 1 else []

    for match in re.finditer(r"(\d+)", row):
        val = int(match.group())
        start = max(0, match.start() - 1)
        end = min(len(row) - 1, match.end())

        for r in range(start, end + 1):
            if above and above[r] not in NOT_SYMBOLS:
                adj[(i - 1, r, above[r])].append(val)
            if below and below[r] not in NOT_SYMBOLS:
                adj[(i + 1, r, below[r])].append(val)
            if r in [start, end] and row[r] not in NOT_SYMBOLS:
                adj[(i, r, row[r])].append(val)


def ans1() -> int:
    return sum([sum(v) for _, v in adj.items()])


def ans2() -> int:
    return sum([prod(v) for k, v in adj.items() if k[2] == "*" and len(v) == 2])


if __name__ == "__main__":
    aoc.print_answer(1, ans1())
    aoc.print_answer(2, ans2())
