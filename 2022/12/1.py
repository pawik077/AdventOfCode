def get_neighbors(map, point):
	neighbors = []
	x, y = point
	if x > 0:
		if ord(map[y][x - 1]) - ord(map[y][x]) <= 1 or map[y][x - 1] == 'E' or map[y][x] == 'S':
			neighbors.append((x - 1, y))
	if x < len(map[0]) - 1:
		if ord(map[y][x + 1]) - ord(map[y][x]) <= 1 or map[y][x + 1] == 'E' or map[y][x] == 'S':
			neighbors.append((x + 1, y))
	if y > 0:
		if ord(map[y - 1][x]) - ord(map[y][x]) <= 1 or map[y - 1][x] == 'E' or map[y][x] == 'S':
			neighbors.append((x, y - 1))
	if y < len(map) - 1:
		if ord(map[y + 1][x]) - ord(map[y][x]) <= 1 or map[y + 1][x] == 'E' or map[y][x] == 'S':
			neighbors.append((x, y + 1))
	return neighbors

# replaced dijkstra with bfs (faster and sufficient)
def bfs(map, start, end):
	distances = {}
	distances[start] = 0

	unvisited = [start]
	while unvisited:
		current = unvisited.pop(0)
		current_steps = distances[current]
		for neighbor in get_neighbors(map, current):
			if neighbor in distances:
				continue
			distances[neighbor] = current_steps + 1
			unvisited.append(neighbor)
			if neighbor == end:
				return current_steps + 1

	return None

with open('input', 'r') as f:
	map = [list(x) for x in f.read().splitlines()]

for row in map:
	if 'S' in row:
		start = (row.index('S'), map.index(row))
	if 'E' in row:
		end = (row.index('E'), map.index(row))

print(bfs(map, start, end))