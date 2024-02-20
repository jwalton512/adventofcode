# solution for 2023 - day 6
from math import ceil, floor, prod

from aoc import aoc

data = aoc.get_input(2023, 6).read_text().splitlines()


def moe(t, d) -> int:
    delta = (t**2 - 4 * d) ** 0.5
    xmin, xmax = (t - delta) / 2, (t + delta) / 2
    return ceil(xmax) - floor(xmin) - 1


def ans1() -> int:
    times, dists = [list(map(int, l[12:].split())) for l in data]
    return prod(map(moe, times, dists))


def ans2() -> int:
    times, dists = [[int(l[12:].replace(" ", ""))] for l in data]
    return prod(map(moe, times, dists))


if __name__ == "__main__":
    aoc.print_answer(1, ans1())
    aoc.print_answer(2, ans2())
