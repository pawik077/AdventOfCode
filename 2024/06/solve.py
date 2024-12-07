import sys

# this one is ugly as a motherfucker, but no way I'm rewriting it

def part1(data):
    data = list(map(list, data))
    pos = [(row, col) for row, sublist in enumerate(data) for col, char in enumerate(sublist) if char in ['v', '>', '<', '^']][0]
    match data[pos[0]][pos[1]]:
        case '^': direction = 0
        case '>': direction = 1
        case 'v': direction = 2
        case '<': direction = 3
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    while(True):
        data[pos[0]][pos[1]] = 'X'
        if not (0 <= pos[0] + dirs[direction][0] < len(data) and 0 <= pos[1] + dirs[direction][1] < len(data[0])):
            break
        if data[pos[0] + dirs[direction][0]][pos[1] + dirs[direction][1]] == '#':
            direction = (direction + 1) % 4
        else:
            pos = (pos[0] + dirs[direction][0], pos[1] + dirs[direction][1])
    return sum(x.count('X') for x in data)

def part2(data):
    data = list(map(list, data))
    data_traversed = [x[:] for x in data]
    start = [(row, col) for row, sublist in enumerate(data_traversed) for col, char in enumerate(sublist) if char in ['v', '>', '<', '^']][0]
    pos = start
    match data[pos[0]][pos[1]]:
        case '^': start_dir = 0
        case '>': start_dir = 1
        case 'v': start_dir = 2
        case '<': start_dir = 3
    direction = start_dir
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    while(True):
        data_traversed[pos[0]][pos[1]] = 'X'
        if not (0 <= pos[0] + dirs[direction][0] < len(data_traversed) and 0 <= pos[1] + dirs[direction][1] < len(data_traversed[0])):
            break
        if data_traversed[pos[0] + dirs[direction][0]][pos[1] + dirs[direction][1]] == '#':
            direction = (direction + 1) % 4
        else:
            pos = (pos[0] + dirs[direction][0], pos[1] + dirs[direction][1])
    visited = [(row, col) for row, sublist in enumerate(data_traversed) for col, char in enumerate(sublist) if char == 'X']
    loops = 0
    for x in visited:
        if x == start: continue
        data_temp = [a[:] for a in data]
        data_temp[x[0]][x[1]] = '#'
        pos = start
        direction = start_dir
        path = []
        while(True):
            path.append((pos[0], pos[1], direction))
            if not (0 <= pos[0] + dirs[direction][0] < len(data_temp) and 0 <= pos[1] + dirs[direction][1] < len(data_temp[0])):
                break
            if data_temp[pos[0] + dirs[direction][0]][pos[1] + dirs[direction][1]] == '#':
                direction = (direction + 1) % 4
                if (pos[0] + dirs[direction][0], pos[1] + dirs[direction][1], direction) in path:
                    loops += 1
                    break
            else:
                pos = (pos[0] + dirs[direction][0], pos[1] + dirs[direction][1])
    return loops

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))
