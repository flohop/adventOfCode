import math


def helper(lines: list[str]):
    # create dict, with two values
    res = {}
    for line in lines:
        st, end = line.split("=")
        end = end.replace("\n", '')
        end = end.strip()
        end = (end[1: len(end)-1]).split(",")
        res[st.strip()] = (end[0].strip(), end[1].strip())

    return res


def solution(lines: list[str]):
    instructions = lines[0].replace("\n", '')

    map_vals = helper(lines[2:])

    cur = "AAA"
    res = 0
    while cur != "ZZZ":
        instr = 0 if instructions[res % len(instructions)] == "L" else 1

        cur = map_vals[cur][instr]
        res += 1
    return res


def solution_two(lines: list[str]):
    instructions = lines[0].replace("\n", '')

    map_vals = helper(lines[2:])

    cur_vals = list(filter(lambda x: x[-1] == "A", map_vals.keys()))
    cycles = []
    ctr = 0
    for cur in cur_vals:
        print("Start at: ", cur)
        res = 0
        while cur[-1] != "Z":
            instr = 0 if instructions[res % len(instructions)] == "L" else 1
            cur = map_vals[cur][instr]
            print("Cur: ",  cur)
            res += 1

        print("============Found res==============")
        cycles.append(res)

    print("Finished")
    return math.lcm(*cycles)



if __name__ == '__main__':
    file_path = "./day_eight.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print(solution_two(lines))
