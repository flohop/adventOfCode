import collections


def hash(s: str):
    res = 0

    for c in s:
        ascii_val = ord(c)

        res += ascii_val
        res *= 17
        res %= 256

    return res


def solution(lines: list[str]):

    values = lines[0].split(",")

    boxes = collections.defaultdict(list)

    for value in values:
        if "=" in value:
            label, focus = value.split("=")
            hash_v = hash(label)
            combined = label + " " + focus

            found_v = False
            for ind, lens in enumerate(boxes[hash_v]):
                if lens.split(" ")[0] == label:
                    boxes[hash_v][ind] = combined
                    found_v = True
                    break

            # label was not there before
            if not found_v:
                boxes[hash_v].append(combined)
        else:
            label, focus = value.split("-")
            hash_v = hash(label)

            for ind, lens in enumerate(boxes[hash_v]):
                if lens.split(" ")[0] == label:
                    boxes[hash_v].remove(lens)
                    break

    res = 0
    for num, boxes in boxes.items():
        if not boxes:
            continue

        for ind, item in enumerate(boxes):
            focal = int(item.split(" ")[1])

            res += (num + 1) * (ind + 1) * focal

    return res


if __name__ == '__main__':
    file_path = "./day_fifteen.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print(solution(lines))