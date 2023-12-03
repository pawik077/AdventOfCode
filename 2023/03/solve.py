import sys

def check_neighbors(data, x, y, end):
    if x > 0:
        if data[y][x-1] != '.': return True
        if y > 0:
            if data[y-1][x-1] != '.': return True
        if y < len(data) - 1:
            if data[y+1][x-1] != '.': return True
    if end < len(data[y]):
        if data[y][end] != '.': return True
        if y > 0:
            if data[y-1][end] != '.': return True
        if y < len(data) - 1:
            if data[y+1][end] != '.': return True
    for i in range(x, end):
        if y > 0:
            if data[y-1][i] != '.':  return True
        if y < len(data) - 1:
            if data[y+1][i] != '.': return True
    return False

def find_numbers(data, x, y):
    numbers = []
    fields = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if 0 <= x + i < len(data[y]) and 0 <= y + j < len(data) and data[y+j][x+i].isdigit()] # 💀
    visited = []
    for field in fields:
        if field in visited: continue
        x = field[0]
        y = field[1]
        end = x
        begin = x
        while end < len(data[y]) and data[y][end].isdigit():
            end += 1
            if (end, y) in fields: visited.append((end, y))
        while begin > 0 and data[y][begin - 1].isdigit():
            begin -= 1
            if (begin, y) in fields: visited.append((begin, y))
        numbers.append(int(data[y][begin:end]))
    return numbers


def part1(data):
    sum = 0
    x = 0
    for y in range(len(data)):
        while x < len(data[y]):
            if data[y][x].isdigit():
                end = x
                while end < len(data[y]) and data[y][end].isdigit():
                    end += 1
                if check_neighbors(data, x, y, end):
                    sum += int(data[y][x:end])
                x = end
            else:
                x += 1
        x = 0
    return sum

def part2(data):
    sum = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '*':
                numbers = find_numbers(data, x, y)
                if len(numbers) == 2:
                    sum += numbers[0] * numbers[1]
    return sum

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))