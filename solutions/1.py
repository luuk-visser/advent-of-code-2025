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
    def instruction_to_turns(instruction):
        direction = 1 if instruction[0] == "R" else -1
        value = int(instruction[1:])
        return direction * value


    def get_positions(instructions, starting_pos=50):
        return np.cumsum(
            np.array([starting_pos] + [instruction_to_turns(instruction) for instruction in instructions])
        )


    instructions = open(input_fp).read().splitlines()
    positions = get_positions(instructions)

    (positions % 100 == 0).sum()
    return (positions,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.cell
def _(positions):
    count = 0
    for prev_pos, curr_pos in zip(positions, positions[1:]):
        if prev_pos > curr_pos:
            count += abs((curr_pos - 1) // 100 - (prev_pos - 1) // 100)
        else:
            count += abs(curr_pos // 100 - prev_pos // 100)
    count
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
