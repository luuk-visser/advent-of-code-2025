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
    def process_intervals(intervals_txt):
        sorted_ivs = sorted(list(map(int, line.split("-"))) for line in intervals_txt.splitlines())
        processed_ivs = [sorted_ivs[0]]
        for iv in sorted_ivs[1:]:
            if iv[0] <= processed_ivs[-1][1] + 1:
                processed_ivs[-1][1] = max(processed_ivs[-1][1], iv[1])
            else:
                processed_ivs.append(iv)
        return np.array(processed_ivs)


    intervals_txt, ingredients_txt = open(input_fp).read()[:-1].split("\n\n")
    ivs = process_intervals(intervals_txt)
    ingredients = list(map(int, ingredients_txt.splitlines()))
    return ingredients, ivs


@app.cell
def _(ingredients, ivs, np):
    def ingredient_in_intervals(ingredient, ivs):
        idx = np.searchsorted(ivs[:, 0], ingredient, "right") - 1
        return idx != -1 and ingredient <= ivs[idx, 1]


    sum(ingredient_in_intervals(ingredient, ivs) for ingredient in ingredients)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.cell
def _(ivs):
    (ivs[:, 1] - ivs[:, 0] + 1).sum()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
