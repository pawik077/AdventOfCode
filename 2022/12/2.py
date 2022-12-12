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

# dijkstra was fucking slow on this one, so used a bfs instead
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

possible_starts = []

for row in map:
	if 'E' in row:
		end = (row.index('E'), map.index(row))

for y in range(len(map)):
	for x in range(len(map[0])):
		if map[y][x] == 'a':
			possible_starts.append((x, y))

print(min([x for x in [bfs(map, start, end) for start in possible_starts] if x is not None]))