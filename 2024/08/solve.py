import sys
import re

def part1(data):
    data = [list(x) for x in data]
    height = len(data)
    width = len(data[0])
    antennas = {char: [(y, x) for y, row in enumerate(data) for x, c in enumerate(row) if c == char] for char in set(re.findall(r'\w|\d', ''.join(''.join(row) for row in data)))}
    antinodes = []
    for frequency in antennas:
        for i, ant_1 in enumerate(antennas[frequency]):
            for ant_2 in antennas[frequency][i+1:]:
                dy = ant_1[0] - ant_2[0]
                dx = ant_1[1] - ant_2[1]
                antinode_a = (ant_1[0] + dy, ant_1[1] + dx)
                antinode_b = (ant_2[0] - dy, ant_2[1] - dx)
                if 0 <= antinode_a[0] < height and 0 <= antinode_a[1] < width:
                    antinodes.append(antinode_a)
                if 0 <= antinode_b[0] < height and 0 <= antinode_b[1] < width:
                    antinodes.append(antinode_b)
    return len(set(antinodes))

def part2(data):
    data = [list(x) for x in data]
    height = len(data)
    width = len(data[0])
    antennas = {char: [(y, x) for y, row in enumerate(data) for x, c in enumerate(row) if c == char] for char in set(re.findall(r'\w|\d', ''.join(''.join(row) for row in data)))}
    antinodes = []
    for frequency in antennas:
        for i, ant_1 in enumerate(antennas[frequency]):
            for ant_2 in antennas[frequency][i+1:]:
                dy = ant_1[0] - ant_2[0]
                dx = ant_1[1] - ant_2[1]
                for i in range(-25,25):
                    antinode_a = (ant_1[0] + dy*i, ant_1[1] + dx*i)
                    antinode_b = (ant_2[0] - dy*i, ant_2[1] - dx*i)
                    if 0 <= antinode_a[0] < height and 0 <= antinode_a[1] < width: antinodes.append(antinode_a)
                    if 0 <= antinode_b[0] < height and 0 <= antinode_b[1] < width: antinodes.append(antinode_b)
    return len(set(antinodes))

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))
