from pathlib import Path

import requests

from advent_of_code_2025.paths import AOC_SESSION, data_dir


def obtain_input(day: int | str, year: int | str = 2025) -> Path:
    """
    Ensure data_dir/day.txt exists by downloading the Advent of Code input if missing.
    Returns the Path to the file.
    """
    data_dir.mkdir(parents=True, exist_ok=True)
    fp = data_dir / f"{day}.txt"

    if fp.exists():
        return fp

    if day == "x":
        fp.write_text("test")
        return fp

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    if not AOC_SESSION:
        raise Exception("File not yet present and no session-cookie available.")
    cookies = {"session": AOC_SESSION}

    response = requests.get(url, cookies=cookies)
    response.raise_for_status()

    # Write to file
    fp.write_text(response.text)

    return fp
