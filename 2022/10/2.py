with open('input', 'r') as f:
	lines = f.read().splitlines()

cycle = 1
x = 1
screen = ''

for i in range(len(lines)):
	screen += ('#' if (abs((cycle - 1) % 40 - x) < 2) else '.')
	screen += ('\n' if (cycle % 40 == 0) else '')
	if lines[i] == 'noop':
		cycle += 1
	elif lines[i].startswith('addx'):
		cycle += 1
		screen += ('#' if (abs((cycle - 1) % 40 - x) < 2) else '.')
		screen += ('\n' if (cycle % 40 == 0) else '')
		cycle += 1
		x += int(lines[i].split(' ')[1])

print(screen)