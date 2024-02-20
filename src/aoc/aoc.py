import os
import re
import sys
from pathlib import Path

import requests

from aoc import log
from aoc.files import input_file, solution_file
from aoc.utils import load_module_from_path


class AocClient:
    def __init__(self):
        self.cookie = os.environ.get("aoc_cookie")
        self.session = requests.Session()
        self.session.cookies.set("session", self.cookie)

    def url(self, year: int, day: int, path: str) -> str:
        return f"https://adventofcode.com/{year}/day/{day}/{path}"

    def get_input(self, year: int, day: int) -> str:
        url = self.url(year, day, "input")
        log.status(f"downloading from {url}")
        resp = self.session.get(url)

        if resp.status_code != 200:
            resp.raise_for_status()
        elif "please identify yourself" in resp.text.lower():
            cookie = os.environ.get("aoc_cookie")
            raise ValueError(f"session cookie invalid ({self.cookie})")

        return resp.text.rstrip("\n")

    def submit_answer(self, year: int, day: int, part: int, answer) -> bool:
        url = self.url(year, day, "answer")
        resp = self.session.post(url, data={"level": part, "answer": answer})
        resp_content = resp.text.lower()

        if "did you already complete it" in resp_content:
            log.error("already completed, or wrong part submitted")
            return False

        if "that's the right answer" in resp_content:
            matches = re.findall(r"rank\s+(\d+)", resp_content)
            if matches:
                log.success(f"right answer! rank {matches[0]}.")
            else:
                log.success(f"right answer!")

            return True

        if "you have to wait" in resp_content:
            matches = re.compile(r"you have ([\w ]+) left to wait").findall(
                resp_content
            )

            if matches:
                log.error(f"submitting too fast, {matches[0]} left to wait.")
            else:
                log.error("submitting too fast")

            return False

        log.status("wrong answer :(")
        return False


def get_input(year: int, day: int) -> Path:
    return input_file(year, day, create_parents_if_not_exists=False)


def print_answer(part: int, answer) -> None:
    print(f"Part {part}: {answer}")


def get_answers(year: int, day: int) -> tuple[int | None, int | None]:
    solution = solution_file(year, day)
    if not solution.exists():
        raise FileNotFoundError

    def call(obj, method: str):
        attr = getattr(obj, method)
        if attr is not None and callable(attr):
            return attr()
        else:
            return None

    module = load_module_from_path(solution, "solution")
    if module:
        ans1, ans2 = call(module, "ans1"), call(module, "ans2")
        return (ans1, ans2)

    return (None, None)


def get_answer(year: int, day: int, part: int) -> int | None:
    return get_answers(year, day)[part - 1]
