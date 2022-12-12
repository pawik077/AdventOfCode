with open('input', 'r') as f:
	data = f.read().splitlines()

score = 0

for i in data:
	if i[2] == 'X':
		score += 1
		if i[0] == 'A':
			score += 3
		elif i[0] == 'C':
			score += 6
	elif i[2] == 'Y':
		score += 2
		if i[0] == 'A':
			score += 6
		elif i[0] == 'B':
			score += 3
	elif i[2] == 'Z':
		score += 3
		if i[0] == 'B':
			score += 6
		elif i[0] == 'C':
			score += 3

print(score)