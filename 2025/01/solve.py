import sys


def part1(data):
    curr = 50
    zero_sum = 0
    for line in data:
        sign = 1 if line[0] == "R" else -1
        dist = int(line[1:]) % 100
        curr = curr + sign * dist
        if curr < 0:
            curr = 100 + curr
        elif curr >= 100:
            curr = curr - 100
        if curr == 0:
            zero_sum += 1
    return zero_sum


def part2(data):
    curr = 50
    zero_sum = 0
    for line in data:
        sign = 1 if line[0] == "R" else -1
        dist = int(line[1:])
        for _ in range(dist):
            curr = curr + sign
            if curr < 0:
                curr = 99
            elif curr >= 100:
                curr = 0
            if curr == 0:
                zero_sum += 1
    return zero_sum


if __name__ == "__main__":
    filename = "input" if "-t" not in sys.argv else "test"
    with open(filename) as f:
        data = f.readlines()
    print(part1(data))
    print(part2(data))
