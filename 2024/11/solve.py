import sys
from collections import Counter

def part1(data):
    data = list(map(int, data))
    for _ in range(25):
        new_data = []
        for stone in data:
            if stone == 0:
                new_data.append(1)
            elif len(str(stone)) % 2 == 0:
                new_data.append(int(str(stone)[:len(str(stone))//2]))
                new_data.append(int(str(stone)[len(str(stone))//2:]))
            else:
                new_data.append(stone * 2024)
        data = new_data
    return len(data)

def part2(data):
    data = Counter(list(map(int,data)))
    for _ in range(75):
        # instead of storing all stones in a list
        # we can just store the count of each stone occurence
        new_data = Counter()
        for stone, count in data.items():
            if stone == 0:
                new_data[1] += count
            elif len(str(stone)) % 2 == 0:
                new_data[int(str(stone)[:len(str(stone))//2])] += count
                new_data[int(str(stone)[len(str(stone))//2:])] += count
            else:
                new_data[stone * 2024] += count
        data = new_data
    return sum(data.values())

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().strip().split(' ')
    print(part1(data))
    print(part2(data))
    