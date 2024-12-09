import sys

def part1(data):
    data = [(int(line.split(':')[0]), list(map(int, line.split(':')[1].split()))) for line in data]
    def is_reachable(subtotal, i):
        if i == len(values) and subtotal == result: return True
        elif subtotal > result or i == len(values): return False
        return is_reachable(subtotal + values[i], i + 1) or is_reachable(subtotal * values[i], i + 1)
    total = 0
    for result, values in data:
        total += result if is_reachable(values[0], 1) else 0
    return total

def part2(data):
    data = [(int(line.split(':')[0]), list(map(int, line.split(':')[1].split()))) for line in data]
    def is_reachable(subtotal, i):
        if i == len(values) and subtotal == result: return True
        elif subtotal > result or i == len(values): return False
        return is_reachable(subtotal + values[i], i + 1) or is_reachable(subtotal * values[i], i + 1) or is_reachable(int(str(subtotal) + str(values[i])), i + 1)
    total = 0
    for result, values in data:
        total += result if is_reachable(values[0], 1) else 0
    return total

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))
    