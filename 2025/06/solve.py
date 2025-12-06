import sys
from math import prod


def part1(data):
    nums = [list(map(int, line.strip().split())) for line in data[:-1]]
    ops = data[-1].strip().split()
    nums = [list(x) for x in zip(*nums)]  # transpose list
    total = 0
    for i, x in enumerate(ops):
        match x:
            case "+":
                total += sum(nums[i])
            case "*":
                total += prod(nums[i])
    return total


def part2(data):
    ops = data[-1].strip().split()
    nums = [list(x) for x in data[:-1]]
    nums = [list(x) for x in zip(*nums)]  # transpose list
    # convert numbers from cephalopod math
    nums_final = []
    problem = []
    for row in nums:
        if all(c.isspace() for c in row):
            nums_final.append(problem)
            problem = []
            continue
        problem.append(int("".join(row)))
    nums_final.append(problem)

    total = 0
    for i, x in enumerate(ops):
        match x:
            case "+":
                total += sum(nums_final[i])
            case "*":
                total += prod(nums_final[i])
    return total


if __name__ == "__main__":
    filename = "input" if "-t" not in sys.argv else "test"
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))
