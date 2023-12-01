
def solution(vals: list[str]):
    res = 0

    for v in vals:
        nums = []
        for c in v:
            if c in "0123456789":
                nums.append(c)

        res += int(nums[0] + nums[-1])
    return res


def solution_part_two(items: list[str]):


    vals = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    res = 0
    for i, l in enumerate(items):
        nums = []
        cur_s = ""
        for c in l:
            if c in "123456789":
                nums.append(c)
                continue
            cur_s += c
            if "one" in cur_s:
                nums.append(vals["one"])
                cur_s = cur_s[-1:]
            elif "two" in cur_s:
                nums.append(vals["two"])
                cur_s = cur_s[-1:]
            elif "three" in cur_s:
                nums.append(vals["three"])
                cur_s = cur_s[-1:]
            elif "four" in cur_s:
                nums.append(vals["four"])
                cur_s = cur_s[-1:]
            elif "five" in cur_s:
                nums.append(vals["five"])
                cur_s = cur_s[-1:]
            elif "six" in cur_s:
                nums.append(vals["six"])
                cur_s = cur_s[-1:]
            elif "seven" in cur_s:
                nums.append(vals["seven"])
                cur_s = cur_s[-1:]
            elif "eight" in cur_s:
                nums.append(vals["eight"])
                cur_s = cur_s[-1:]
            elif "nine" in cur_s:
                nums.append(vals["nine"])
                cur_s = cur_s[-1:]

        res += int(nums[0] + nums[-1])

    return res


if __name__ == '__main__':

    file_path = "day_one_part_two.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print(solution_part_two(lines))

