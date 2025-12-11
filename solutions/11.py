import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    from collections import defaultdict
    from functools import cache
    from pathlib import Path

    import marimo as mo

    from advent_of_code_2025.utils import obtain_input
    return Path, cache, defaultdict, mo, obtain_input


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
def _(defaultdict, input_fp):
    def get_adj_list(input_fp):
        lines = open(input_fp).read().splitlines()
        return defaultdict(
            list, {line[: line.index(":")]: line[line.index(":") + 2 :].split(" ") for line in lines}
        )


    adj_list = get_adj_list(input_fp)
    return (adj_list,)


@app.cell
def _(adj_list, cache):
    @cache
    def n_paths_to_out(src):
        if src == "out":
            return 1

        return sum(n_paths_to_out(dest) for dest in adj_list[src])


    n_paths_to_out("you")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.cell
def _(adj_list, cache):
    @cache
    def n_paths_to_out_via_stops(src, visited_dac, visited_fft):
        if src == "out":
            return visited_dac and visited_fft

        return sum(
            n_paths_to_out_via_stops(dest, visited_dac or src == "dac", visited_fft or src == "fft")
            for dest in adj_list[src]
        )


    n_paths_to_out_via_stops("svr", False, False)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
