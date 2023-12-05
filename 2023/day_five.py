def helper(lines: list[str]) -> list:
    """Given a section return the dict for it """
    i = 1
    res = {}
    while i < len(lines):
        if lines[i] == "\n":
            i += 1
            continue

        # at start of a block
        map_name = lines[i].split()[0]

        values = []
        # get a list of all values
        i += 1
        while i < len(lines) and lines[i] != "\n":
            values.append([int(x) for x in lines[i].split()])
            i += 1

        res[map_name] = values

    return res


def solution(lines: list[str]):
    og_seeds = [[int(x), int(x)] for x in lines[0].split(":")[1].split()]

    val_dict = helper(lines)

    map_names = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

    # Get tuple (seed, soil)
    for ind in range(len(og_seeds)):

        for map_name in map_names:
            for dst, src, rng in val_dict[map_name]:
                if og_seeds[ind][1] >= src > og_seeds[ind][1] - rng:
                    y = og_seeds[ind][1] - src
                    og_seeds[ind][1] = dst + y
                    break

    res = min(og_seeds, key=lambda x: x[1])
    return res[1]


def solution_part_two(lines: list[str]):
    # Could be clever and reverse the process, but I gotta get to work...
    og_seeds = [int(x) for x in lines[0].split(":")[1].split()]

    new_seeds = []
    i = 0
    while i < len(og_seeds):
        start = og_seeds[i]
        rng = og_seeds[i + 1]

        new_seeds += [[x, x] for x in list(range(start, start+rng))]
        i += 2

    og_seeds = new_seeds

    val_dict = helper(lines)

    map_names = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

    # Get tuple (seed, next_v)
    for ind in range(len(og_seeds)):

        for map_name in map_names:
            for dst, src, rng in val_dict[map_name]:
                if og_seeds[ind][1] >= src > og_seeds[ind][1] - rng:
                    y = og_seeds[ind][1] - src
                    og_seeds[ind][1] = dst + y
                    break

    res = min(og_seeds, key=lambda x: x[1])
    return res[1]


if __name__ == '__main__':
    file_path = "day_five.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print(solution_part_two(lines))
