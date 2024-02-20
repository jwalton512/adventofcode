from pathlib import Path


def _path(path: str | Path, create_if_not_exists: bool = False) -> Path:
    if isinstance(path, str):
        path = Path(path)

    if create_if_not_exists:
        path.mkdir(parents=True, exist_ok=True)

    return path


def project_root() -> Path:
    return Path(__file__).parent.parent.parent.resolve()


def events_dir(year: int, create_if_not_exists: bool = False) -> Path:
    return _path(project_root().joinpath("events", str(year)), create_if_not_exists)


def inputs_dir(year: int, create_if_not_exists: bool = False) -> Path:
    return _path(events_dir(year).joinpath("inputs"), create_if_not_exists)


def solutions_dir(year: int, create_if_not_exists: bool = False) -> Path:
    return _path(events_dir(year).joinpath("solutions"), create_if_not_exists)


def solution_file(
    year: int, day: int, create_parents_if_not_exists: bool = False
) -> Path:
    return solutions_dir(
        year, create_if_not_exists=create_parents_if_not_exists
    ).joinpath(f"day{str(day).zfill(2)}.py")


def solution_template() -> Path:
    return Path(__file__).parent.joinpath("template", "solution.txt")


def input_file(year: int, day: int, create_parents_if_not_exists: bool = False) -> Path:
    return inputs_dir(year, create_if_not_exists=create_parents_if_not_exists).joinpath(
        f"day{str(day).zfill(2)}.txt"
    )
