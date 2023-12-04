

def helper(line: str):
    numbers = line.split(":")[1]

    p1, p2 = numbers.split("|")

    s1 = set()
    s2 = set()

    p1 = p1.split()
    p2 = p2.split()

    for n in p1:
        s1.add(int(n))

    for n in p2:
        s2.add(int(n))

    return s1, s2


def solution_part_two(lines: list[str]):

    matches = []
    times = [1] * len(lines)

    for l in lines:
        s1, s2 = helper(l)
        inter = s1.intersection(s2)
        matches.append(len(inter))

    for i in range(len(lines)):
        m = matches[i]
        for j in range(1, m+1):
            if i+ j >= len(times):
                continue

            times[i+j] += times[i]

    return sum(times)


def solution(lines: list[str]):
    res = 0

    for line in lines:
        s1, s2 = helper(line)

        inter = s1.intersection(s2)
        if len(inter) > 0:
            res += 2 ** (len(inter)-1)

    return res


if __name__ == '__main__':
    file_path = "day_four.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print(solution_part_two(lines))
