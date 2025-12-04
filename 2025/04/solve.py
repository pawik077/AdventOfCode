import sys

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def count_adjacent(grid, i, j):
    return sum(
        1
        for dx, dy in DIRECTIONS
        if 0 <= i + dx < len(grid)
        and 0 <= j + dy < len(grid[0])
        and grid[i + dx][j + dy] == "@"
    )


def part1(data):
    data = [list(x) for x in data]
    return len(
        [
            (i, j)
            for i in range(len(data))
            for j in range(len(data[i]))
            if data[i][j] == "@" and count_adjacent(data, i, j) < 4
        ]
    )


def part2(data):
    data = [list(x) for x in data]
    total_rolls = 0
    while True:
        removable = [
            (i, j)
            for i in range(len(data))
            for j in range(len(data[i]))
            if data[i][j] == "@" and count_adjacent(data, i, j) < 4
        ]
        if not removable:
            break
        total_rolls += len(removable)
        for i, j in removable:
            data[i][j] = "."
    return total_rolls


if __name__ == "__main__":
    filename = "input" if "-t" not in sys.argv else "test"
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))
