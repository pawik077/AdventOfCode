from math import floor, log10
import sys


def part1(data):
    ranges = data.strip().split(",")
    ids = []
    invalid_ids = []
    for r in ranges:
        start, end = map(int, r.split("-"))
        ids.extend(list(range(start, end + 1)))
    for id in ids:
        d = floor(log10(id)) + 1  # length of the id
        left = id // (10 ** (d // 2))
        right = id % (10 ** (d // 2))
        if left == right:
            invalid_ids.append(id)
    return sum(invalid_ids)


def part2(data):
    ranges = data.strip().split(",")
    ids = []
    invalid_ids = []
    for r in ranges:
        start, end = map(int, r.split("-"))
        ids.extend(list(range(start, end + 1)))
    for id in ids:
        s = str(id)
        L = len(s)
        # divide into blocks of size d
        # then multiply to get the original string
        for d in range(1, L):
            if L % d != 0:
                continue
            block = s[:d]
            if block * (L // d) == s:
                invalid_ids.append(id)
                break
    return sum(invalid_ids)


if __name__ == "__main__":
    filename = "input" if "-t" not in sys.argv else "test"
    with open(filename) as f:
        data = f.read()
    print(part1(data))
    print(part2(data))
