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
    def parse_data(input_fp):
        data = open(input_fp).read().split("\n\n")
        shape_data = data[:-1]
        shapes = (
            np.array([[list(line) for line in shape.splitlines()[1:]] for shape in shape_data]) == "#"
        )
        region_data = data[-1]
        regions = [
            (
                np.array(line[: line.index(":")].split("x"), dtype="int"),
                np.array(line[line.index(":") + 2 :].split(" "), dtype="int"),
            )
            for line in region_data.splitlines()
        ]
        return shapes, regions


    shapes, regions = parse_data(input_fp)
    return regions, shapes


@app.cell
def _(regions, shapes):
    shape_sizes = shapes.sum(axis=(1, 2))
    print(sum([region[0].prod() - (region[1] * shape_sizes).sum() > 0 for region in regions]))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
