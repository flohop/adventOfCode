
def solution_part_two(lines: list[str]):
    visited = set()
    res = 0

    def helper(row: int, col: int, cur_nums: list[int]):
        if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
            return

        if lines[row][col] not in "0123456789":
            return

        # go as far left as possible
        while col > 0 and lines[row][col-1] in "0123456789":
            col -= 1

        # check if num has already been added
        if (row, col) in visited:
            return

        visited.add((row, col))

        cur_num = ""
        # get the num
        while col <= len(lines[row]) and lines[row][col] in "0123456789":
            cur_num += lines[row][col]
            col += 1

        if len(cur_num) > 0:
            cur_nums.append(int(cur_num))

    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == "\n":
                continue
            if c not in ".0123456789":
                cur_nums = []
                helper(row - 1, col, cur_nums)  # top
                helper(row + 1, col, cur_nums)  # bot
                helper(row, col - 1, cur_nums)  # left
                helper(row, col + 1, cur_nums)  # right
                helper(row - 1, col - 1, cur_nums)  # top - left
                helper(row - 1, col + 1, cur_nums)  # top -right
                helper(row + 1, col - 1, cur_nums)  # bot -left
                helper(row + 1, col + 1, cur_nums)  # bot - right

                if len(cur_nums) == 2:
                    res += cur_nums[0] * cur_nums[1]
    return res

def solution(lines: list[str]):
    res = 0

    visited = set()

    def helper(row: int, col: int):
        nonlocal res

        if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
            return

        if lines[row][col] not in "0123456789":
            return

        # go as far left as possible
        while col > 0 and lines[row][col-1] in "0123456789":
            col -= 1

        # check if num has already been added
        if (row, col) in visited:
            return

        visited.add((row, col))

        cur_num = ""
        # get the num
        while col <= len(lines[row]) and lines[row][col] in "0123456789":
            cur_num += lines[row][col]
            col += 1

        if len(cur_num) > 0:
            cur_num = int(cur_num)
            res += cur_num

    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == "\n":
                continue
            if c not in ".0123456789":
                helper(row - 1, col)  # top
                helper(row + 1, col)  # bot
                helper(row, col - 1)  # left
                helper(row, col + 1)  # right
                helper(row - 1, col - 1)  # top - left
                helper(row - 1, col + 1)  # top -right
                helper(row + 1, col - 1)  # bot -left
                helper(row + 1, col + 1)  # bot - right

    return res


if __name__ == '__main__':
    file_path = "./day_three.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print(solution_part_two(lines))
