import sys

def part1(l1, l2):
    return sum([abs(a-b) for a, b in zip(sorted(l1), sorted(l2))])

def part2(l1, l2):
    return sum([a * l2.count(a) for a in l1])

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.readlines()
    l1, l2 = map(list, zip(*[map(int, x.split()) for x in data]))
    print(part1(l1, l2))
    print(part2(l1, l2))