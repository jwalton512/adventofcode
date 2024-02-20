from typing import Any

from click import secho


def status(msg: Any) -> None:
    secho(msg, fg="white")


def success(msg: Any) -> None:
    secho(msg, fg="green")


def error(msg: Any) -> None:
    secho(msg, fg="red", bold=True)
