import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from pathlib import Path

    from advent_of_code_2025.utils import obtain_input

    import numpy as np
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
    lines = open(input_fp).read().splitlines()
    line_data = np.array([line.split() for line in lines])
    ops = line_data[-1]
    return line_data, lines, ops


@app.cell
def _(line_data, ops):
    numbers = line_data[:-1].astype(int)
    numbers[:, ops == "+"].sum() + numbers[:, ops == "*"].prod(axis=0).sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.cell
def _(lines, np, ops):
    transposed_lines = np.array(["".join(lst) for lst in zip(*lines[:-1])])
    split_idcs = np.empty(ops.size + 1, dtype="int")
    split_idcs[0] = -1
    split_idcs[1:-1] = np.nonzero(transposed_lines == " " * len(transposed_lines[0]))[0]
    split_idcs[-1] = len(transposed_lines)

    grouped_numbers = [
        transposed_lines[start + 1 : end].astype(int) for start, end in zip(split_idcs, split_idcs[1:])
    ]

    sum(group.sum() if op == "+" else group.prod() for group, op in zip(grouped_numbers, ops))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
