import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    from itertools import chain
    from pathlib import Path

    import marimo as mo

    from advent_of_code_2025.utils import obtain_input

    return Path, chain, mo, obtain_input


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
def _():
    def n_digits(num):
        return len(str(num))

    def ceiling_division(n, d):
        return -(n // -d)

    def generate_repeated_numbers(l, r, n_reps=2):
        init_seq_len = ceiling_division(n_digits(l), n_reps)
        if n_digits(l) < init_seq_len * n_reps:
            sequence = str(10 ** (init_seq_len - 1))
        else:
            sequence = str(l)[:init_seq_len]
            if int(sequence * n_reps) < l:
                sequence = str(int(sequence) + 1)

        while (curr := int(sequence * n_reps)) <= r:
            yield curr
            sequence = str(int(sequence) + 1)

    return generate_repeated_numbers, n_digits


@app.cell
def _(input_fp):
    id_ranges = [[int(num) for num in nums.split("-")] for nums in open(input_fp).read().split(",")]
    return (id_ranges,)


@app.cell
def _(chain, generate_repeated_numbers, id_ranges):
    invalid_id_sum_doubled = sum(
        chain.from_iterable(generate_repeated_numbers(l, r, n_reps=2) for l, r in id_ranges)
    )

    invalid_id_sum_doubled
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.cell
def _(chain, generate_repeated_numbers, id_ranges, n_digits):
    invalid_id_sum_repeated = sum(
        set(
            chain.from_iterable(
                generate_repeated_numbers(l, r, n_reps=n_reps)
                for l, r in id_ranges
                for n_reps in range(2, n_digits(r) + 1)
            )
        )
    )
    invalid_id_sum_repeated
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
