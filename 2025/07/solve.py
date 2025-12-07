import sys


def part1(data):
    data = [list(x) for x in data]
    splits = 0
    start = (0, data[0].index("S"))
    data[1][start[1]] = "|"
    for y in range(1, len(data) - 1):
        for x in range(len(data[0])):
            if data[y][x] == "|":
                if data[y + 1][x] == ".":
                    data[y + 1][x] = "|"
                elif data[y + 1][x] == "^":
                    splits += 1
                    data[y + 1][x + 1] = "|"
                    data[y + 1][x - 1] = "|"
    return splits


def part2(data):
    data = [list(x) for x in data]
    start = (0, data[0].index("S"))
    data[1][start[1]] = 1
    for y in range(1, len(data) - 1):
        for x in range(len(data[0])):
            # each path carries the count of different ways to reach it
            if isinstance(data[y][x], int):
                if data[y + 1][x] == ".":
                    data[y + 1][x] = data[y][x]
                # if paths merge, sum their counts
                elif isinstance(data[y + 1][x], int):
                    data[y + 1][x] += data[y][x]
                # if they split, distribute the count to both paths
                elif data[y + 1][x] == "^":
                    data[y + 1][x + 1] = (
                        data[y + 1][x + 1] + data[y][x]
                        if isinstance(data[y + 1][x + 1], int)
                        else data[y][x]
                    )
                    data[y + 1][x - 1] = (
                        data[y + 1][x - 1] + data[y][x]
                        if isinstance(data[y + 1][x - 1], int)
                        else data[y][x]
                    )
    return sum([x for x in data[-1] if isinstance(x, int)])


if __name__ == "__main__":
    filename = "input" if "-t" not in sys.argv else "test"
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))
