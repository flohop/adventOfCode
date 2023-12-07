import collections


def get_rank(s1: str):
    # 7 -> Five of a kind
    # 6 -> FOur of a kind
    # 5 -> Full house
    # 4 -> Three of a kind
    # 3 -> Two pairs
    # 2 -> One pair
    # 1 - High card

    counter = collections.defaultdict(int)  #
    if s1 == "JJJJJ":
        return 7

    for c in s1:
        counter[c] += 1

    # For every Joker
    if "J" in counter.keys():
        nums = counter["J"]
        items = list(filter(lambda x: x[0] != "J", list(counter.items())))
        items.sort(key=lambda x: (x[1], get_value(x[0])), reverse=True)

        s1 = s1.replace("J", items[0][0])

        counter[items[0][0]] += nums
        del counter["J"]

    # check for five
    if counter[s1[0]] == 5:
        return 7

    # four
    if counter[s1[0]] == 4 or counter[s1[1]] == 4:
        return 6

    values = list(counter.values())

    len_values = 0
    for v in values:
        if v != 0:
            len_values += 1

    if len_values == 2 and (values[0] == 2 or values[0] == 3) and (values[1] == 2 or values[1] == 3):
        return 5

    if len_values == 3 and values[0] == 3 or values[1] == 3 or values[2] == 3:
        return 4

    if len_values == 3 and (values[0] == 2 and values[1] == 2) or (values[0] == 2 and values[2] == 2) or (values[1] == 2 and values[2] == 2):
        return 3

    if len_values == 4:
        return 2

    return 1


def get_value(c1):
    """
    Creat a string of the value that represents it's value
    1 -> A
    2 -> B
    ...
    """

    com_dict = {
        "A": "O",
        "K": "N",
        "Q": "M",
        "T": "K",
        "9": "J",
        "8": "I",
        "7": "H",
        "6": "G",
        "5": "F",
        "4": "E",
        "3": "D",
        "2": "C",
        "1": "B",
        "J": "A"
    }

    res = ""
    for c in c1:
        res += com_dict[c]
    return res


def solution(lines: list[str]):
    card_value = {}
    for line in lines:
        card, amount = line.split()
        card_value[card] = int(amount)

    all_cards = list(card_value.keys())
    all_cards.sort(key=lambda x: (get_rank(x), get_value(x)), reverse=True)

    res = 0
    for i, c in enumerate(all_cards):
        cur_num = len(all_cards) - i
        res += cur_num * card_value[c]

    return res


if __name__ == '__main__':
    file_path = "./day_seven.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print(solution(lines))