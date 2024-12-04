import sys

def bounds(data, x, y):
    return 0 <= y < len(data) and 0 <= x < len(data[y])

def part1(data):
    word = 'XMAS'
    directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    result = 0 
    for y in range(len(data)):
        for x in range(len(data[y])):
            for dx, dy in directions:
                for i in range(len(word)):
                    if not bounds(data, x + i*dx, y + i*dy) or data[y + i*dy][x + i*dx] != word[i]:
                        break
                else:
                    result += 1
    return result

def part2(data):
    a_s = [(y,x) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == 'A' and bounds(data, y + 1, x + 1)] # A is not at the edge
    result = 0
    for a in a_s:
        # Check if the corners are M and S
        corners = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
        corners = [(a[0] + dy, a[1] + dx) for dy, dx in corners]
        corners = [data[y][x] for y, x in corners]
        if corners[0] == 'M' and corners[1] == 'S' or corners[0] == 'S' and corners[1] == 'M':
            if corners[2] == 'M' and corners[3] == 'S' or corners[2] == 'S' and corners[3] == 'M':
                result += 1
    return result

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))
    