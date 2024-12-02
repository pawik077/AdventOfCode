import sys

def isSafe(levels):
    if (sorted(levels) != levels) and (sorted(levels, reverse=True) != levels):
        return False
    for i, level in enumerate(levels):
        if i == 0:
            continue
        if not (1 <= abs(level - levels[i-1]) <= 3):
            return False
    return True

def part1(data):
    safe = 0
    for report in data:
        levels = list(map(int, report.split()))
        if isSafe(levels):
            safe += 1
    return safe

def part2(data):
    safe = 0
    for report in data:
        levels = list(map(int, report.split()))
        for idx in range(-1, len(levels)):
            levels_cleared = [x for i,x in enumerate(levels) if i!=idx]
            if isSafe(levels_cleared):
                safe += 1
                break
    return safe
 
if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.readlines()
    print(part1(data))
    print(part2(data))
    