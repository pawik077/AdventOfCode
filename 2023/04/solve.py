import sys
from collections import Counter

def part1(data):
    sum = 0
    for line in data:
        nums = line.split(':')[1].split('|')
        cardNums = set(map(int, nums[0].split()))
        winningNums = set(map(int, nums[1].split()))
        sum += int(2 ** (len(cardNums & winningNums) - 1))
    return sum

def part2(data):
    count = Counter()
    for n, card in enumerate(data):
        nums = card.split(':')[1].split('|')
        count[n + 1] += 1
        cardNums = set(map(int, nums[0].split()))
        winningNums = set(map(int, nums[1].split()))
        for x in range(len(cardNums & winningNums)):
            count[n + 2 + x] += count[n + 1]
    return count.total()

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))