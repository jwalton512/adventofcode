# solution for 2023 - day 2
import re

from aoc import aoc

data = aoc.get_input(2023, 2).read_text().splitlines()

answer1 = answer2 = 0

for line in data:
    gid, game = line.split(": ")
    gid = int(gid[5:])
    maxr = maxg = maxb = 0

    for n, c in re.findall(r"(\d+) (red|green|blue)", game):
        n = int(n)
        if c == "red":
            maxr = max(n, maxr)
        elif c == "green":
            maxg = max(n, maxg)
        elif c == "blue":
            maxb = max(n, maxb)

    answer1 += gid * (maxr <= 12 and maxg <= 13 and maxb <= 14)
    answer2 += maxr * maxg * maxb


def ans1() -> int:
    return answer1


def ans2() -> int:
    return answer2


if __name__ == "__main__":
    aoc.print_answer(1, ans1())
    aoc.print_answer(2, ans2())
