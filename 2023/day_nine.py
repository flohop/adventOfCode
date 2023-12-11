
def get_seq(line: str):

    cur = [int(x) for x in line.split()]
    res = [cur]
    next = []

    not_finished = True
    while not_finished:
        num_zeroes = 0
        for i in range(0, len(cur)-1):
            val = cur[i+1] - cur[i]
            if val == 0:
                num_zeroes += 1

            next.append(val)

        not_finished = num_zeroes != len(next)
        res.append(next)

        cur = next
        next = []

    return res


def extrapolate(values: list[list[int]]):

    values[-1].append(0)

    for i in reversed(range(0, len(values)- 1)):
        new_val = values[i][-1] + values[i+1][-1]
        values[i].append(new_val)

    return values[0][-1]


def extrapolate_two(values: list[list[int]]):

    values[-1].insert(0, 0)

    for i in reversed(range(0, len(values) - 1)):
        new_val = values[i][0] - values[i+1][0]
        values[i].insert(0, new_val)

    return values[0][0]


def solution(lines: list[str]):
    res = 0

    for line in lines:
        line = line.replace("\n", '')
        seq = get_seq(line)
        val = extrapolate(seq)
        res += val

    return res


if __name__ == '__main__':
    file_path = "./day_nine.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    #lines = ["1 3 6 10 15 21"]
    print(solution(lines))