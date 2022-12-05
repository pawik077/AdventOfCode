with open('input', 'r') as f:
	data = f.read().splitlines()

score = 0

for i in data:
	if i[2] == 'X':
		score += 0
		if i[0] == 'A':
			score += 3
		elif i[0] == 'B':
			score += 1
		elif i[0] == 'C':
			score += 2
	elif i[2] == 'Y':
		score += 3
		if i[0] == 'A':
			score += 1
		elif i[0] == 'B':
			score += 2
		elif i[0] == 'C':
			score += 3
	elif i[2] == 'Z':
		score += 6
		if i[0] == 'A':
			score += 2
		elif i[0] == 'B':
			score += 3
		elif i[0] == 'C':
			score += 1

print(score)