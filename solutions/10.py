import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    from itertools import product
    from pathlib import Path

    import marimo as mo
    import numpy as np
    import sympy

    from advent_of_code_2025.utils import obtain_input
    return Path, mo, np, obtain_input, product, sympy


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
def _(np):
    def parse_line(line):
        light_configuration = np.array(list(line[1 : line.index("]")])) == "#"
        button_tuples = eval(
            line[line.index("]") + 1 : line.index("{") - 1].replace(")", ",)").replace(") (", "),(")
        )
        joltage_requirements = np.array(
            line[line.index("{") + 1 : line.index("}")].split(","), dtype=int
        )
        return light_configuration, button_tuples, joltage_requirements
    return (parse_line,)


@app.cell
def _(input_fp, np, parse_line, product):
    def fewest_presses_lights(line):
        light_configuration, button_tuples = parse_line(line)[:2]
        buttons = np.zeros((len(button_tuples), light_configuration.size), dtype=int)
        for i, button_tup in enumerate(button_tuples):
            buttons[i, button_tup] = 1

        return min(
            sum(booleans)
            for booleans in product([False, True], repeat=buttons.shape[0])
            if (buttons[np.array(booleans)].sum(axis=0) % 2 == light_configuration).all()
        )


    data = open(input_fp).read().splitlines()
    sum(fewest_presses_lights(line) for line in data)
    return (data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$A \in \mathbb{Z}^{m \times n}_{\geq 0}, v \in \mathbb{Z}^n_{\geq 0} \\
    \min(||x||_1) : Ax = v , x \in \mathbb{Z}^m_{\geq 0}$$
    """)
    return


@app.cell
def _(data, np, parse_line, product, sympy):
    def is_integer(x, tol=1e-9):
        return abs(x - round(x)) < tol


    def solve_matrix_nonnegative_integer(A, b):
        m, n = A.shape
        x = sympy.symbols(f"x:{n}", integer=True, nonnegative=True)

        solution_set = sympy.linsolve((sympy.Matrix(A), sympy.Matrix(b)), *x)
        solution_tuple = list(solution_set)[0]
        free_vars = list({v for expr in solution_tuple for v in expr.free_symbols})
        if not free_vars:
            yield solution_tuple
            return

        def max_val(var):
            idx = int(var.name[1:])
            return b[A[:, idx].astype(bool)].min()

        ranges = [range(max_val(var) + 1) for var in free_vars]

        eval_func = sympy.lambdify(free_vars, solution_tuple)

        for var_vals in product(*ranges):
            evaluations = eval_func(*var_vals)
            if all(is_integer(evaluation) for evaluation in evaluations):
                evaluations = [int(round(evaluation)) for evaluation in evaluations]
                if all(evaluation >= 0 for evaluation in evaluations):
                    yield evaluations


    def fewest_presses_joltage(line):
        parsed_data = parse_line(line)[1:]
        button_tuples = parsed_data[0]

        # Joltage requirements, final result
        b = parsed_data[1]

        # Matrix transforming button presses (x) into joltage levels
        A = np.zeros((b.size, len(button_tuples)), dtype=int)
        for i, button_tup in enumerate(button_tuples):
            A[button_tup, i] = 1

        return min(sum(solution) for solution in solve_matrix_nonnegative_integer(A, b))


    sum(fewest_presses_joltage(line) for line in data)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
