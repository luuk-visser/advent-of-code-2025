import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path

    import marimo as mo
    import numpy as np

    from advent_of_code_2025.utils import obtain_input

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
    def count_surrounding_rolls(grid, i, j):
        return (
            sum(
                grid[p, q]
                for p in range(max(0, i - 1), min(i + 2, n))
                for q in range(max(0, j - 1), min(j + 2, m))
            )
            - grid[i, j]
        )

    def is_accessible_paper(grid, i, j):
        return grid[i, j] and count_surrounding_rolls(grid, i, j) < 4

    grid = np.array([list(line) for line in open(input_fp).read().splitlines()]) == "@"
    n, m = grid.shape
    sum(is_accessible_paper(grid, i, j) for i in range(n) for j in range(m))
    return grid, is_accessible_paper, m, n


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.cell
def _(grid, is_accessible_paper, m, n):
    reduced_grid = grid.copy()
    prev_count = reduced_grid.sum() + 1
    while reduced_grid.sum() < prev_count:
        prev_count = reduced_grid.sum()
        for i in range(n):
            for j in range(m):
                if is_accessible_paper(reduced_grid, i, j):
                    reduced_grid[i, j] = 0
    grid.sum() - reduced_grid.sum()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
