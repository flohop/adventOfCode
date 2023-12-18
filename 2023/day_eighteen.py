
def helper_two(lines: list[str]):
    res = []
    for line in lines:
        line = line.replace("\n", '')
        _, _, clr = line.split()
        clr = clr[1: -1]
        dir = int(clr[-1])
        length = int(clr[1:len(clr)-1], 16)
        res.append((dir, length))

    return res

def helper(lines: list[str]):
    res = []
    for line in lines:
        line = line.replace("\n", '')
        direction, dist, clr = line.split()
        res.append((direction, int(dist), clr[1:-1]))

    return res



def solution(lines: list[str]) -> int:

    instructions = helper(lines)

    dir_map = {
        "R": (0, 1), # R, C
        "L": (0, -1),
        "U": (-1, 0),
        "D": (1, 0)
    }

    x, y = 0, 0  # cur position
    area = 0
    outer = 0
    for direc, length, clr in instructions:
        dy, dx = dir_map[direc]
        dx, dy = dx * length, dy * length
        x, y = x + dx, y + dy
        outer += length
        area += x * dy # super weird theorem I had to look up
    return area + outer // 2 + 1  # got  hint from reddit for the theorem

def solution_part_two(lines: list[str]) -> int:

    instructions = helper_two(lines)

    dir_map = {
        0: (0, 1), # R, C
        2: (0, -1),
        3: (-1, 0),
        1: (1, 0)
    }

    x, y = 0, 0  # cur position
    area = 0
    outer = 0
    for direc, length in instructions:
        dy, dx = dir_map[direc]
        dx, dy = dx * length, dy * length
        x, y = x + dx, y + dy
        outer += length
        area += x * dy # super weird theorem I had to look up
    return area + outer // 2 + 1  # got  hint from reddit for the theore




if __name__ == '__main__':
    file_path = "./day_eighteen.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print(solution_part_two(lines))
