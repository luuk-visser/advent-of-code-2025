import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path

    import marimo as mo
    import numpy as np

    from advent_of_code_2025.utils import obtain_input

    # from advent_of_code_2025.grid import GridPoint, Direction, rotate_right
    return Path, mo, np, obtain_input


@app.cell
def _(Path, obtain_input):
    day_number = Path(__file__).stem
    input_fp = obtain_input(day_number)
    return day_number, input_fp


@app.cell(hide_code=True)
def _(day_number, mo):
    mo.md(f"""
    # Day {day_number}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 1
    """)
    return


@app.cell
def _(input_fp, np):
    batteries = np.asarray([list(map(int, r)) for r in open(input_fp).read().splitlines()])

    def largest_possible_joltage(bank, n_batteries=2):
        idcs_per_digit = [np.nonzero(bank == i)[0] for i in range(10)]
        joltage = 0
        l = 0
        for rem_batteries in range(n_batteries, 0, -1):
            r = bank.size - rem_batteries
            for num, digit_idcs in reversed(list(enumerate(idcs_per_digit))):
                idx_in_idcs = np.searchsorted(digit_idcs, l, side="left")
                if idx_in_idcs == len(digit_idcs):
                    continue

                battery_idx = digit_idcs[idx_in_idcs]
                if battery_idx > r:
                    continue

                joltage = joltage * 10 + num
                l = battery_idx + 1
                break

        return joltage

    sum(largest_possible_joltage(bank, n_batteries=2) for bank in batteries)
    return batteries, largest_possible_joltage


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.cell
def _(batteries, largest_possible_joltage):
    sum(largest_possible_joltage(bank, n_batteries=12) for bank in batteries)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
