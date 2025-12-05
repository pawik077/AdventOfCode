import sys


def part1(data):
    ranges = [
        (int(x), int(y))
        for ran in data[: data.index("")]
        for (x, y) in [ran.split("-")]
    ]
    ids = list(map(int, data[data.index("") + 1 :]))
    fresh = 0
    for id in ids:
        for x, y in ranges:
            if x <= id <= y:
                fresh += 1
                break
    return fresh


def part2(data):
    ranges = [
        (int(x), int(y))
        for ran in data[: data.index("")]
        for (x, y) in [ran.split("-")]
    ]
    ranges.sort()
    merged = []
    curr_start, curr_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= curr_end + 1:
            curr_end = max(curr_end, end)
        else:
            merged.append((curr_start, curr_end))
            curr_start, curr_end = start, end
    merged.append((curr_start, curr_end))

    return sum(e - s + 1 for s, e in merged)


if __name__ == "__main__":
    filename = "input" if "-t" not in sys.argv else "test"
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))
