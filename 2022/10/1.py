with open('input', 'r') as f:
	lines = f.read().splitlines()

cycle = 1
x = 1
sum = 0

for i in range(len(lines)):
	if cycle % 40 == 20:
		sum += x * cycle
	if lines[i] == 'noop':
		cycle += 1
	elif lines[i].startswith('addx'):
		cycle += 1
		if cycle % 40 == 20:
			sum += x * cycle
		cycle += 1
		x += int(lines[i].split(' ')[1])

print(sum)