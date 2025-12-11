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
    tile_coords = np.loadtxt(input_fp, dtype="int", delimiter=",")
    return (tile_coords,)


@app.cell
def _(tile_coords):
    def area(c1, c2):
        return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)


    max(area(c1, c2) for c1 in tile_coords for c2 in tile_coords)
    return (area,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.cell
def _(area, np, tile_coords):
    def get_line_segments(points):
        return zip(points, np.roll(points, shift=-1, axis=0))


    def max_area_inside_loop(tile_coords):
        sorted_rectangles = sorted(
            [
                ((c1, c2), area(c1, c2))
                for i, c1 in enumerate(tile_coords)
                for j, c2 in enumerate(tile_coords[i + 1 :])
            ],
            key=lambda item: item[1],
            reverse=True,
        )
        line_segments = list(get_line_segments(tile_coords))
        horizontal_segments = [
            (
                p1,
                p2,
            )
            for p1, p2 in line_segments
            if (p2 - p1)[0] == 0
        ]
        vertical_segments = [
            (
                p1,
                p2,
            )
            for p1, p2 in line_segments
            if (p2 - p1)[1] == 0
        ]

        def rect_is_inside_loop(r1, r2):
            y1, x1 = np.minimum(r1, r2) + 0.01
            y2, x2 = np.maximum(r1, r2) - 0.01

            for y_ray in (y1, y2):
                n_left = 0
                n_right = 0
                for p1, p2 in vertical_segments:
                    if min(p1[0], p2[0]) <= y_ray and y_ray <= max(p1[0], p2[0]):
                        if p1[1] <= x1:
                            n_left += 1
                        elif p1[1] >= x2:
                            n_right += 1
                        else:
                            return False
                if n_left % 2 == 0:
                    return False
            for x_ray in (x1, x2):
                for p1, p2 in horizontal_segments:
                    if min(p1[1], p2[1]) <= x_ray and x_ray <= max(p1[1], p2[1]):
                        if y1 < p1[0] and p1[0] < y2:
                            return False

            return True

        for (r1, r2), rect_area in sorted_rectangles:
            if rect_is_inside_loop(r1, r2):
                return rect_area


    max_area_inside_loop(tile_coords)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
