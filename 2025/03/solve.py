import sys


def part1(data):
    data = [list(map(int, list(x))) for x in data]
    total = 0
    for bank in data:
        dec = max(bank[:-1])
        ones = max(bank[bank.index(dec) + 1 :])
        joltage = dec * 10 + ones
        total += joltage
    return total


def part2(data):
    data = [list(map(int, list(x))) for x in data]
    total = 0
    K = 12
    for bank in data:
        stack = []
        discards = len(bank) - K  # cause we want K digits
        for x in bank:
            while stack and x > stack[-1] and discards > 0:
                stack.pop()
                discards -= 1
            stack.append(x)
        joltage = int("".join(map(str, stack[:K])))
        total += joltage
    return total


if __name__ == "__main__":
    filename = "input" if "-t" not in sys.argv else "test"
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))
