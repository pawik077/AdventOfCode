import sys
import re

def part1(data):
    data = re.findall(r'mul\(\d{1,3},\d{1,3}\)', ''.join(data))
    data = [tuple(map(int, re.findall(r'\d{1,3}', x))) for x in data]
    return sum([x * y for x, y in data])

def part2(data):
    data = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", ''.join(data))
    done = []
    do = True
    for x in data:
        if x == "do()": do = True
        elif x == "don't()": do = False
        elif do:
            x, y = tuple(map(int, re.findall(r'\d{1,3}', x)))
            done.append(x * y)
    return sum(done)

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.readlines()
    print(part1(data))
    print(part2(data))
    