import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from pathlib import Path

    from advent_of_code_2025.graph import UnionFindBySize
    from advent_of_code_2025.utils import obtain_input

    import numpy as np
    return Path, UnionFindBySize, mo, np, obtain_input


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
    def n_largest(arr, n):
        return np.partition(arr, -n)[-n:]


    def get_connections_sorted_by_dist(box_coords):
        dists = np.square(box_coords[:, np.newaxis] - box_coords[np.newaxis, :]).sum(axis=-1)

        triu_idcs = np.triu_indices_from(dists, k=1)
        flattened_dists = dists[triu_idcs]

        flattened_sorted_idcs = flattened_dists.argsort()
        return np.array(triu_idcs).T[flattened_sorted_idcs]


    box_coords = np.loadtxt(input_fp, dtype="int", delimiter=",")
    n_nodes = box_coords.shape[0]
    connections_sorted_by_dist = get_connections_sorted_by_dist(box_coords)
    return box_coords, connections_sorted_by_dist, n_largest, n_nodes


@app.cell
def _(UnionFindBySize, connections_sorted_by_dist, n_largest, n_nodes, np):
    def part_one():
        uf = UnionFindBySize(n_nodes)
        for u, v in connections_sorted_by_dist[:1000]:
            uf.union_sets(u, v)

        # Select root nodes and obtain sizes
        sizes = np.array([uf.sizes[i] for i in range(n_nodes) if i == uf.parents[i]])

        return n_largest(sizes, 3).prod()


    part_one()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.cell
def _(UnionFindBySize, box_coords, connections_sorted_by_dist, n_nodes):
    def part_two():
        uf2 = UnionFindBySize(n_nodes)
        for u, v in connections_sorted_by_dist:
            uf2.union_sets(u, v)
            if uf2.n_components == 1:
                return box_coords[u, 0] * box_coords[v, 0]


    part_two()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
