import sys
from math import lcm

def part1(data):
    path = data[0]
    graph = {line.split(' = ')[0]: (line.split(' = ')[1].split(', ')[0][1:], line.split(' = ')[1].split(', ')[1][:-1]) for line in data[2:]}
    steps = 0
    current = 'AAA'
    while current != 'ZZZ':
        match path[steps % len(path)]:
            case 'L': current = graph[current][0]
            case 'R': current = graph[current][1]
        steps += 1
    return steps

def part2(data):
    path = data[0]
    graph = {line.split(' = ')[0]: (line.split(' = ')[1].split(', ')[0][1:], line.split(' = ')[1].split(', ')[1][:-1]) for line in data[2:]}
    allSteps = []
    currents = [k for k in graph.keys() if k[2] == 'A']
    for c in currents:
        steps = 0
        while c[-1] != 'Z':
            c = graph[c][0] if path[steps % len(path)] == 'L' else graph[c][1]
            steps += 1
        allSteps.append(steps)
    # why it works: https://www.reddit.com/r/adventofcode/comments/18e6vdf/2023_day_8_part_2_an_explanation_for_why_the/
    return lcm(*allSteps) 

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))