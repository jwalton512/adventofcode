# solution for 2023 - day 5
from collections import deque

from aoc import aoc

sections = aoc.get_input(2023, 5).read_text().split("\n\n")
seeds = list(map(int, sections.pop(0)[7:].split()))

maps = []
for section in sections:
    maps.append(
        [
            (s, s + l, d - s)
            for d, s, l in [map(int, line.split()) for line in section.splitlines()[1:]]
        ]
    )


# I came up with a brute force solution that worked, but it took several hours to run
# Part 2. I knew there had to be a better solution that ignored the impossible seeds
# Final solution mostly from: https://github.com/mebeim/aoc/tree/master/2023#part-2-4
def solve(segments: deque) -> int:
    for map_ in maps:
        processed = deque()
        while segments:
            a, b = segments.popleft()

            for c, d, delta in map_:
                part_l = c <= a < d
                part_r = c < b <= d

                if part_l and part_r:
                    processed.append((a + delta, b + delta))
                    break
                elif part_l:
                    processed.append((a + delta, d + delta))
                    segments.append((d, b))
                    break
                elif part_r:
                    processed.append((c + delta, b + delta))
                    segments.append((a, c))
                    break
                elif a < c and b > d:
                    processed.append((c + delta, d + delta))
                    segments.append((a, c))
                    segments.append((d, b))
                    break
            else:
                processed.append((a, b))

        segments = processed

    return min([s[0] for s in segments])


def ans1() -> int:
    return solve(deque((s, s + 1) for s in seeds))


def ans2() -> int:
    segments = deque((a, a + b) for a, b in zip(seeds[::2], seeds[1::2]))
    return solve(segments=segments)


if __name__ == "__main__":
    aoc.print_answer(1, ans1())
    aoc.print_answer(2, ans2())
