# solution for 2023 - day 1
import re

from aoc import aoc

data = aoc.get_input(2023, 1).read_text().splitlines()


def str_to_int(inp: str, words=False) -> int:
    nums = {}
    n = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }

    w = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    n = n | w if words else n

    for k, v in n.items():
        for m in re.finditer(rf"{k}", inp):
            nums[m.start()] = v

    vals = [v for _, v in sorted(nums.items())]
    return int(vals[0] + vals[-1])


def ans1() -> int:
    return sum([str_to_int(line) for line in data])


def ans2() -> int:
    return sum([str_to_int(line, words=True) for line in data])


if __name__ == "__main__":
    aoc.print_answer(1, ans1())
    aoc.print_answer(2, ans2())
