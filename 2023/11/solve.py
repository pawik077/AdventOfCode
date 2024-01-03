import sys

def part1(data):
    i = 0
    while i < len(data):
        if not '#' in data[i]:
            data.insert(i, data[i])
            i += 1
        i += 1
    data = list(map(list, zip(*data)))
    i = 0
    while i < len(data):
        if not '#' in data[i]:
            data.insert(i, data[i])
            i += 1
        i += 1
    data = list(map(list, zip(*data)))
    galaxies = {}
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == '#':
                galaxies[len(galaxies)] = (x, y)
    paths = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            paths.append(abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]))
    return sum(paths)

def part2(data):
    return None

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))