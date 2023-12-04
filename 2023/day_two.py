

def helper(line: str):
    """
    Given a string return list of games and id
    :param line:
    :return:
    """

    game_id = line.split(":")[0][5:]
    games_s = line.split(":")[1].split(";")

    games = []  # tuples of (r, g, b)

    for game_s in games_s:
        draws = game_s.split(",")
        rgb = [0, 0, 0] # rgb
        for draw in draws:
            if "red" in draw:
                ind = 0
            elif "green" in draw:
                ind = 1
            elif "blue":
                ind = 2

            rgb[ind] = int(draw.split()[0])

        games.append(rgb)

    return {"game_id": int(game_id), "games": games}


def solution(lines: list[str]):
    NUM_RED = 12
    NUM_GREEN = 13
    NUM_BLUE = 14

    res = 0

    for line in lines:
        game_id, games = helper(line).values()
        is_possible = True
        for r, g, b in games:
            if r > NUM_RED or g > NUM_GREEN or b > NUM_BLUE:
                is_possible = False

        if is_possible:
            res += game_id

    return res

def solution_part_two(lines: list[str]):
    res = 0

    for line in lines:
        max_r = 1
        max_g = 1
        max_b = 1
        game_id, games = helper(line).values()
        for r, g, b in games:
            max_r = max(r, max_r)
            max_g = max(g, max_g)
            max_b = max(b, max_b)

        res += (max_r * max_g * max_b)

    return res


if __name__ == '__main__':
    file_path = "./day_two.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print(solution_part_two(lines))
