import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from pathlib import Path

    from advent_of_code_2025.utils import obtain_input

    import numpy as np
    import polars as pl

    # from advent_of_code_2025.grid import GridPoint, Direction, rotate_right
    return Path, mo, obtain_input


@app.cell
def _(Path, obtain_input):
    day_number = Path(__file__).stem
    input_fp = obtain_input(day_number)
    return (day_number,)


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
def _():
    # data = open(input_fp).read()
    # data = open(input_fp).read().splitlines()
    # data = np.loadtxt(input_fp, dtype="int")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
