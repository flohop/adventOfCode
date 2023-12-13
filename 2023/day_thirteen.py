
def get_groups(lines: list[str]):
    res = []

    cur = []
    for l in lines:
        l = l.replace("\n", '')
        if not l:
            res.append(list(cur))
            cur = []
        else:
            cur.append(list(l))
    res.append(cur)
    return res


def solution(lines: list[str]):
    groups = get_groups(lines)
    res = 0

    for group in groups:
        # check for vertical mirror
        possible_col = [x for x in range(1, len(group[0]))]

        for row in group:
            good_pos = []

            for i in possible_col:
                part_size = min(i, len(row) - i)

                if row[i-part_size:i] == list(reversed(row[i:i+part_size])):
                    good_pos.append(i)

            possible_col = good_pos

        for val in possible_col:
            res += val

        # check for horizontal
        possible_row = [x for x in range(1, len(group))]

        for c in range(len(group[0])):
            good_pos = []

            for i in possible_row:
                part_size = min(i, len(group) - i)
                # check pos

                # get left side of mirror
                left_side = []
                for j in range(i-part_size, i):
                    left_side.append(group[j][c])

                right_side = []
                for j in reversed(range(i, i+part_size)):
                    right_side.append(group[j][c])

                if right_side == left_side:
                    good_pos.append(i)
            possible_row = good_pos

        for val in possible_row:
            res += val * 100

    return res


def solution_part_two(lines: list[str]):
    groups = get_groups(lines)
    res = 0

    for group in groups:
        # check for vertical mirror
        possible_col = [x for x in range(1, len(group[0]))]

        # reverse loop
        # check every possible position and count how manay wrongs there are

        good_pos = []
        for pos in possible_col:
            diff = 0
            for row in group:
                part_size = min(pos, len(row)- pos)

                left_side = row[pos-part_size:pos]
                right_side = list(reversed(row[pos:pos+part_size]))

                for x in range(len(left_side)):
                    if left_side[x] != right_side[x]:
                        diff += 1
            if diff == 1:
                good_pos.append(pos)

        for val in good_pos:
            res += val

        if len(good_pos) > 0:
            continue

        # check for horizontal
        possible_row = [x for x in range(1, len(group))]

        for pos in possible_row:
            diff = 0

            for c in range(len(group[0])):
                part_size = min(pos, len(group) - pos)
                # check pos

                # get left side of mirror
                left_side = []
                for j in range(pos-part_size, pos):
                    left_side.append(group[j][c])

                right_side = []
                for j in reversed(range(pos, pos+part_size)):
                    right_side.append(group[j][c])

                for x in range(len(left_side)):
                    if left_side[x] != right_side[x]:
                        diff += 1

            if diff == 1:
                good_pos.append(pos)

        for val in good_pos:
            res += val * 100

    return res


if __name__ == '__main__':
    file_path = "./day_thirteen.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print("One: ", solution(lines))
    print("Two: ", solution_part_two(lines))