import sys

def get_moves(position, data):
    char = data[position[1]][position[0]]
    moves = []
    match char:
        case 'S':
            if data[position[1] - 1][position[0]] in ('|', 'F', '7'):
                moves.append((position[0], position[1] - 1))
            if data[position[1] + 1][position[0]] in ('|', 'L', 'J'):
                moves.append((position[0], position[1] + 1))
            if data[position[1]][position[0] - 1] in ('-', 'F', 'L'):
                moves.append((position[0] - 1, position[1]))
            if data[position[1]][position[0] + 1] in ('-', '7', 'J'):
                moves.append((position[0] + 1, position[1]))
        case '|':
            if data[position[1] - 1][position[0]] in ('|', 'F', '7'):
                moves.append((position[0], position[1] - 1))
            if data[position[1] + 1][position[0]] in ('|', 'L', 'J'):
                moves.append((position[0], position[1] + 1))
        case '-':
            if data[position[1]][position[0] - 1] in ('-', 'F', 'L'):
                moves.append((position[0] - 1, position[1]))
            if data[position[1]][position[0] + 1] in ('-', '7', 'J'):
                moves.append((position[0] + 1, position[1]))
        case 'L':
            if data[position[1] - 1][position[0]] in ('|', 'F', '7'):
                moves.append((position[0], position[1] - 1))
            if data[position[1]][position[0] + 1] in ('-', '7', 'J'):
                moves.append((position[0] + 1, position[1]))
        case 'J':
            if data[position[1] - 1][position[0]] in ('|', 'F', '7'):
                moves.append((position[0], position[1] - 1))
            if data[position[1]][position[0] - 1] in ('-', 'F', 'L'):
                moves.append((position[0] - 1, position[1]))
        case '7':
            if data[position[1] + 1][position[0]] in ('|', 'L', 'J'):
                moves.append((position[0], position[1] + 1))
            if data[position[1]][position[0] - 1] in ('-', 'F', 'L'):
                moves.append((position[0] - 1, position[1]))
        case 'F':
            if data[position[1] + 1][position[0]] in ('|', 'L', 'J'):
                moves.append((position[0], position[1] + 1))
            if data[position[1]][position[0] + 1] in ('-', '7', 'J'):
                moves.append((position[0] + 1, position[1]))
    return moves

def part1(data):
    start = (-1,-1)
    for line in data:
        if line.find('S') != -1:
            start = (line.find('S'), data.index(line))
            break
    currents = [start, start]
    visited = []
    steps = 0
    while currents[0] != currents[1] or len(visited) == 0:
        visited.append(currents[0])
        visited.append(currents[1])
        moves1 = get_moves(currents[0], data)
        moves2 = get_moves(currents[1], data)
        if data[currents[0][1]][currents[0][0]] == 'S':
            currents[0] = moves1[0]
            currents[1] = moves2[1]
        else:
            currents[0] = moves1[0] if moves1[0] not in visited else moves1[1]
            currents[1] = moves2[0] if moves2[0] not in visited else moves2[1]
        steps += 1
    return steps

def part2(data):
    return None

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))