import copy
def helper(lines: list[str]) -> list[list[str]]:
    res = []

    for line in lines:
        line = line.replace("\n", '')
        res.append(list(line))

    return res


def move_north(grid: list[list[str]]):
    ROWS, COLS = len(grid), len(grid[0])
    for c in range(COLS):
        for r in range(ROWS):
            # swap with previous row until 0 or # reached
            if grid[r][c] != "O":
                continue
            i = 1
            while r - i >= 0 and grid[r - i][c] == ".":
                grid[r - i + 1][c], grid[r - i][c] = grid[r - i][c], grid[r - i + 1][c]
                i += 1

    res = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "O":
                res += (ROWS - r)


def move_south(grid: list[list[str]]):
    ROWS, COLS = len(grid), len(grid[0])
    for c in range(COLS):
        for r in reversed(range(ROWS)):

            # swap with previous row until 0 or # reached
            if grid[r][c] != "O":
                continue
            i = 1
            while r + i < ROWS and grid[r + i][c] == ".":
                grid[r + i - 1][c], grid[r + i][c] = grid[r + i][c], grid[r + i - 1][c]
                i += 1

    return grid


def move_east(grid: list[list[str]]):

    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in reversed(range(COLS)):

            # swap with previous row until 0 or # reached
            if grid[r][c] != "O":
                continue
            i = 1
            while c + i < COLS and grid[r][c+i] == ".":
                grid[r][c+i-1], grid[r][c+i] = grid[r][c+i], grid[r][c+i-1]
                i += 1

    return grid


def move_west(grid: list[list[str]]):

    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):

            # swap with previous row until 0 or # reached
            if grid[r][c] != "O":
                continue
            i = 1
            while c - i >= 0 and grid[r][c-i] == ".":
                grid[r][c-i+1], grid[r][c-i] = grid[r][c-i], grid[r][c-i+1]
                i += 1

    return grid


def solution(lines: list[str]):

    grid = helper(lines)

    memo = []

    times = 1000
    for i in range(times):
        move_north(grid)
        move_west(grid)
        move_south(grid)
        move_east(grid)



    res = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "O":
                res += (len(grid) - r)

    return res

if __name__ == '__main__':
    file_path = "./day_fourteen.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print("One: ", solution(lines))
    #print("Two: ", solution_part_two(lines))