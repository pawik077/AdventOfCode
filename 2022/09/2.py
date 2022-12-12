with open('input', 'r') as f:
	data = f.readlines()

knots = [(0, 0) for i in range(10)]
history = [knots[9]]

for line in data:
	for i in range(int(line[2:])):
		match line[0]:
			case 'R': 
				knots[0] = (knots[0][0] + 1, knots[0][1])
			case 'L':
				knots[0] = (knots[0][0] - 1, knots[0][1])
			case 'U':
				knots[0] = (knots[0][0], knots[0][1] + 1)
			case 'D':
				knots[0] = (knots[0][0], knots[0][1] - 1)
		for i in range(1, len(knots)):
			if abs(knots[i][0] - knots[i - 1][0]) > 1 or abs(knots[i][1] - knots[i - 1][1]) > 1:
				if knots[i][0] < knots[i - 1][0]:
					knots[i] = (knots[i][0] + 1, knots[i][1])
				if knots[i][0] > knots[i - 1][0]:
					knots[i] = (knots[i][0] - 1, knots[i][1])
				if knots[i][1] < knots[i - 1][1]:
					knots[i] = (knots[i][0], knots[i][1] + 1)
				if knots[i][1] > knots[i - 1][1]:
					knots[i] = (knots[i][0], knots[i][1] - 1)
		if knots[9] not in history:
			history.append(knots[9])

print(len(history))
