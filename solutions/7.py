import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    from collections import defaultdict
    from pathlib import Path

    import marimo as mo

    from advent_of_code_2025.utils import obtain_input

    # from advent_of_code_2025.grid import GridPoint, Direction, rotate_right
    return Path, defaultdict, mo, obtain_input


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
def _(input_fp):
    lines = open(input_fp).read().splitlines()

    def n_beam_splits(lines):
        n, m = len(lines), len(lines[0])
        start = lines[0].index("S")
        beams = set([start])
        n_splits = 0

        for i in range(1, n):
            for col in list(beams):
                if lines[i][col] == "^":
                    n_splits += 1
                    beams.remove(col)

                    beams.add(col - 1)
                    beams.add(col + 1)

        return n_splits

    n_beam_splits(lines)
    return (lines,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.cell
def _(defaultdict, lines):
    def n_particles(lines):
        n, m = len(lines), len(lines[0])

        start = lines[0].index("S")
        particles = defaultdict(int)
        particles[start] = 1

        for i in range(1, n):
            for col, count in list(particles.items()):
                if lines[i][col] == "^":
                    del particles[col]

                    particles[col - 1] += count
                    particles[col + 1] += count

        return sum(particles.values())

    n_particles(lines)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
