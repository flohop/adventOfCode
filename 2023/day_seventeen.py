import collections
import heapq


def helper(lines: list[str]):
    """Create a connected graph"""

    lines = [[int(n) for n in x if n != "\n"] for x in lines]
    res = {}

    ROWS, COLS = len(lines), len(lines[0])

    ctr = 0
    for r in range(ROWS):
        for c in range(COLS):
            neighs = []
            # go three left
            l = 1
            cost_left = 0
            while c - l >= 0 and l <= 3:
                cost_left += lines[r][c-l]
                neighs.append((cost_left, ctr - l))
                l += 1

            # go three right
            right = 1
            cost_right = 0
            while c + right < COLS and right <= 3:
                cost_right += lines[r][c+right]
                neighs.append((cost_right, ctr + right))
                right += 1

            # go three up
            u = 1
            cost_up = 0
            while r - u >= 0 and u <= 3:
                cost_up += lines[r-u][c]
                neighs.append((cost_up, ctr - COLS * u))
                u += 1

            # go three down
            d = 1
            cost_down = 0
            while r + d < ROWS and d <= 3:
                cost_down += lines[r+d][c]
                neighs.append((cost_down, ctr + COLS * d))
                d += 1

            res[ctr] = list(neighs)
            ctr += 1

    return res


def solution():
    from heapq import heappop, heappush
    ll = [[int(y) for y in x] for x in open('./day_seventeen.txt').read().strip().split('\n')]
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def inr(pos, arr):
        return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))

    def run(mindist, maxdist):
        # cost, x, y, disallowedDirection
        q = [(0, 0, 0, -1)]
        seen = set()
        costs = {}
        while q:
            cost, x, y, dd = heappop(q)
            if x == len(ll) - 1 and y == len(ll[0]) - 1:  # goal x, goal y
                return cost
            if (x, y, dd) in seen:
                continue
            seen.add((x, y, dd))
            for direction in range(4):
                costincrease = 0
                if direction == dd or (direction + 2) % 4 == dd:
                    # can't go this way
                    continue
                for distance in range(1, maxdist + 1):
                    xx = x + DIRS[direction][0] * distance
                    yy = y + DIRS[direction][1] * distance
                    if inr((xx, yy), ll):
                        costincrease += ll[xx][yy]
                        if distance < mindist:
                            continue
                        nc = cost + costincrease
                        if costs.get((xx, yy, direction), 1e100) <= nc:
                            continue
                        costs[(xx, yy, direction)] = nc
                        heappush(q, (nc, xx, yy, direction))

    print(run(1, 3))
    print(run(4, 10))


if __name__ == '__main__':
    solution()
