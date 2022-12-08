with open('input', 'r') as f:
	data = [list(map(int, x)) for x in [l.strip() for l in f.readlines()]]

max_visibility = 0

for i in range(len(data)):
	for j in range(len(data[i])):
		if i == 0 or i == len(data) - 1 or j == 0 or j == len(data[i]) - 1:
			continue
		visibility = [0, 0, 0, 0]
		for t in reversed(data[i][:j]):
			visibility[0] += 1
			if t >= data[i][j]:
				break
		for t in data[i][j+1:]:
			visibility[1] += 1
			if t >= data[i][j]:
				break
		for t in reversed([row[j] for row in data][:i]):
			visibility[2] += 1
			if t >= data[i][j]:
				break
		for t in [row[j] for row in data][i+1:]:
			visibility[3] += 1
			if t >= data[i][j]:
				break
		max_visibility = max(max_visibility, visibility[0] * visibility[1] * visibility[2] * visibility[3])

print(max_visibility)