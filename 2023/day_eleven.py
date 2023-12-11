import itertools


def expand_universe(lines: list[str]):

    grid = [list(x.replace("\n", '')) for x in lines]

    ROWS, COLS = len(grid), len(grid[0])

    rows = []
    cols = []

    # find rows
    for r in range(ROWS):
        only_points = True
        for c in range(COLS):
            if grid[r][c] != ".":
                only_points = False

        if only_points:
            rows.append(r)

    # find cols
    for c in range(COLS):
        only_points = True
        for r in range(ROWS):
            if grid[r][c] != ".":
                only_points = False

        if only_points:
            cols.append(c)

    for i, r in enumerate(rows):
        grid.insert(i + r, ["."] * COLS)

    for i, c in enumerate(cols):
        for r in range(len(grid)):
            grid[r].insert(i+c, ".")

    return grid


def solution(lines: list[str]):

    grid = expand_universe(lines)

    ROWS, COLS = len(grid), len(grid[0])

    res = []
    stars = []  # (r, c)
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "#":
                stars.append((r, c))

    for i, (x_one, y_one) in enumerate(stars):
        for j in range(i+1, len(stars)):
            x_two, y_two = stars[j]

            res.append(sum([abs(x_one - x_two), abs(y_one - y_two)]))

    return sum(res)


def solution_part_two(lines: list[str]):
    grid = [list(x.replace("\n", '')) for x in lines]

    ROWS, COLS = len(grid), len(grid[0])

    rows = []
    cols = []

    MILLION = 1_000_000

    # Find expanded rows, cols.
    # If a row or col is between two points add 100
    # find rows
    for r in range(ROWS):
        only_points = True
        for c in range(COLS):
            if grid[r][c] != ".":
                only_points = False

        if only_points:
            rows.append(r)

    # find cols
    for c in range(COLS):
        only_points = True
        for r in range(ROWS):
            if grid[r][c] != ".":
                only_points = False

        if only_points:
            cols.append(c)

    res = 0
    stars = []  # (r, c)
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "#":
                stars.append((r, c))

    for i, (x_one, y_one) in enumerate(stars):
        for j in range(i+1, len(stars)):
            x_two, y_two = stars[j]

            for empty_x in rows:
                if x_one < empty_x < x_two or x_two < empty_x < x_one:
                    res += MILLION - 1

            for empty_y in cols:
                if y_one < empty_y < y_two or y_two < empty_y < y_one:
                    res += MILLION - 1

            res += (sum([abs(x_one - x_two), abs(y_one - y_two)]))

    return res


if __name__ == '__main__':
    file_path = "day_eleven.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()


    print(solution_part_two(lines))
    print(solution(lines))