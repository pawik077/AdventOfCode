import sys

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

def part1(data):
    data = [[int(x) for x in line] for line in data]
    trailheads = [(y, x) for y, row in enumerate(data) for x, cell in enumerate(row) if cell == 0]
    def bfs(start): # BFS: returns set of all 9s reachable from start
        queue = [start]
        visited = set()
        nines = set()
        while queue:
            position = queue.pop(0)
            if position in visited:
                continue
            visited.add(position)
            y, x = position
            if data[y][x] == 9:
                nines.add(position)
            for dy, dx in dirs:
                if 0 <= y + dy < len(data) and 0 <= x + dx < len(data[0]) and data[y + dy][x + dx] - data[y][x] == 1:
                    queue.append((y + dy,x + dx))
        return nines
    return sum([len(bfs(trailhead)) for trailhead in trailheads])
 
def part2(data):
    data = [[int(x) for x in line] for line in data]
    trailheads = [(y, x) for y, row in enumerate(data) for x, cell in enumerate(row) if cell == 0]
    def dfs(start, visited): # DFS: returns number of paths from start to 9
        y, x = start
        if data[y][x] == 9:
            return 1
        visited.add(start)
        count = 0
        for dy, dx in dirs:
            if 0 <= y + dy < len(data) and 0 <= x + dx < len(data[0]) and (y + dy,x + dx) not in visited and data[y + dy][x + dx] - data[y][x] == 1:
                count += dfs((y+dy,x+dx), visited)
        visited.remove(start)
        return count
    return sum([dfs(trailhead, set()) for trailhead in trailheads])

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))
    