import sys

def solution(data, reverse = False):
    sum = 0
    for line in data:
        # both parts are basically the same, except part 2 is reversed
        diffs = [line] if not reverse else [list(reversed(line))]
        while not all([x == 0 for x in diffs[-1]]):
            dif = []
            for i in range(len(diffs[-1]) - 1):
                dif.append(diffs[-1][i + 1] - diffs[-1][i])
            diffs.append(dif)
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].append(diffs[i + 1][-1] + diffs[i][-1])
        sum += diffs[0][-1]
    return sum

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = [[int(x) for x in line.split()] for line in f.read().splitlines()]
    print(solution(data))
    print(solution(data, reverse=True))