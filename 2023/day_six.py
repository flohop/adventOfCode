from functools import reduce


def helper(lines: list[str]):
    """
    Always expect two lines
    """
    times = [int(x) for x in lines[0].split(":")[1].split()]
    distance = [int(x) for x in lines[1].split(":")[1].split()]

    return list(zip(times, distance))

def helper_2(lines: list[str]):
    """
    Always expect two lines
    """
    times = int(''.join(lines[0].split(":")[1].split()))
    distance = int(''.join(lines[1].split(":")[1].split()))

    return [(times, distance)]


def solution(lines: list[str]):
    race_values = helper_2(lines)

    ways_to_win = []

    for time, rec_dist in race_values:
        ways = 0
        for speed in range(1, time):
            rem_time = time - speed

            if speed * rem_time > rec_dist:
                ways += 1

        ways_to_win.append(ways)

    return reduce(lambda x, y: x*y, ways_to_win)


if __name__ == '__main__':
    file_path = "./day_six.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print(solution(lines))