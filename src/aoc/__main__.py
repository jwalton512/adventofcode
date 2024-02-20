import os
import sys
from datetime import datetime
from string import Template

import click
from requests import HTTPError

from aoc import log
from aoc.aoc import AocClient, get_answer, get_answers
from aoc.files import input_file, solution_file, solution_template


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "-y",
    "--year",
    type=int,
    default=lambda: datetime.now().year,
    help="year of puzzle to start.",
)
@click.option(
    "-d", "--day", type=click.IntRange(min=1, max=25), help="day of puzzle to start."
)
def start(year: int, day: int | None = None):
    now = datetime.now()
    current_year = now.year
    current_day = now.day
    current_month = now.month
    if day is None:
        if year != current_year:
            log.error(f"day required if year not equal to {current_year}")
            sys.exit(0)
        elif not (1 <= current_day <= 25 and current_month == 12):
            log.error(f"day not provided, and {current_year} event not active")
            sys.exit(0)
        day = current_day

    solution = solution_file(year, day, create_parents_if_not_exists=True)
    if not solution.exists():
        with open(solution_template(), "r") as f:
            template = Template(f.read())
            content = template.substitute({"year": year, "day": day})
            solution.write_text(content)
            log.success(f"solution file created: {solution}")

    input_ = input_file(year, day, create_parents_if_not_exists=True)
    if not input_.exists():
        try:
            log.status("getting input")
            inp = AocClient().get_input(year, day)
        except (HTTPError, ValueError) as e:
            log.error(e)
            sys.exit(0)

        with open(input_, "w") as f:
            f.write(inp)

        log.success(f"input file created: {input_}")


@cli.command()
@click.option(
    "-y",
    "--year",
    type=int,
    default=lambda: datetime.now().year,
    help="year of puzzle to run.",
)
@click.option(
    "-d", "--day", type=click.IntRange(min=1, max=25), help="day of puzzle to run."
)
def run(year: int, day: int):
    try:
        answers = get_answers(year, day)
    except FileNotFoundError:
        log.error(f"No solution found for {year} day {day}")
        sys.exit(0)

    print(f"Part 1: {answers[0]}")
    print(f"Part 2: {answers[1]}")


def validate_part(ctx, param, value):
    if value in [1, 2]:
        return value

    raise click.BadParameter("part must be 1 or 2")


@cli.command()
@click.option(
    "-y",
    "--year",
    type=int,
    default=lambda: datetime.now().year,
    help="year of puzzle to run.",
)
@click.option(
    "-d",
    "--day",
    type=click.IntRange(min=1, max=25),
    required=True,
    help="day of puzzle to run.",
)
@click.option(
    "-p",
    "--part",
    type=int,
    required=True,
    callback=validate_part,
    help="part to submit (1 or 2)",
    default=1,
)
def submit(year: int, day: int, part: int):
    try:
        answer = get_answer(year, day, part)
    except FileNotFoundError:
        log.error(f"No solution found for {year} day {day}")
        sys.exit(0)

    if answer is None:
        log.error(f"no answer for: {year} day {day} part {part}")
        sys.exit(0)
    try:
        log.status(f"submitting answer for {year} day {day} - {answer}")
        AocClient().submit_answer(year, day, part, answer)
    except (HTTPError, ValueError) as e:
        log.error(e)
        sys.exit(0)


if __name__ == "__main__":
    cli()
