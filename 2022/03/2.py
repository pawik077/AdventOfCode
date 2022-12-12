def get_priority(char):
	return ord(char) - 96 if char.islower() else ord(char) - 38

with open('input', 'r') as f:
	data = f.read().splitlines()
priorities = 0

split = []
for i in range(0, len(data), 3):
	split.append(data[i:i+3])

for block in split:
	seen = []
	for char in block[0]:
		if char in block[1] and char in block[2] and char not in seen:
			priorities += get_priority(char)
			seen.append(char)

print(priorities)