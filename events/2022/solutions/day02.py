# solution for 2022 - day 2
from aoc import aoc

table = bytes.maketrans(b"ABCXYZ", b"036012")
data = aoc.get_input(2022, 2).read_bytes().translate(table)


# each outcome (our_play + result) results in a unique value
# by using translation table and a matrix of values, we can
# easily determine the score of each round
def score(matrix: tuple) -> int:
    score = 0
    for line in data.splitlines():
        i = sum(map(int, line.split()))
        score += matrix[i]

    return score


def ans1() -> int:
    return score((4, 8, 3, 1, 5, 9, 7, 2, 6))


def ans2() -> int:
    return score((3, 4, 8, 1, 5, 9, 2, 6, 7))


if __name__ == "__main__":
    aoc.print_answer(1, ans1())
    aoc.print_answer(2, ans2())
