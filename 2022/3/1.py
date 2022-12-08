def get_priority(char):
	return ord(char) - 96 if char.islower() else ord(char) - 38

with open('input', 'r') as f:
	data = f.read().splitlines()

priorities = 0

for line in data:
	first, second = line[:len(line)//2], line[len(line)//2:]
	seen = []
	for i in first:
		if i in second and i not in seen:
			priorities += get_priority(i)
			seen.append(i)

print(priorities)