with open('input', 'r') as f:
	data = [list(map(int, x)) for x in [l.strip() for l in f.readlines()]]

visible = 0

for i in range(len(data)):
	for j in range(len(data[i])):
		if i == 0 or i == len(data) - 1 or j == 0 or j == len(data[i]) - 1:
			visible += 1
			continue
		if (all(x < data[i][j] for x in data[i][:j])):
			visible += 1
			continue
		if (all(x < data[i][j] for x in data[i][j+1:])):
			visible += 1
			continue
		if (all(x < data[i][j] for x in [row[j] for row in data][:i])):
			visible += 1
			continue
		if (all(x < data[i][j] for x in [row[j] for row in data][i+1:])):
			visible += 1
			continue

print(visible)