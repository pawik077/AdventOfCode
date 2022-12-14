with open('input', 'r') as f:
	rocks = [[(int(a.split(',')[0]), int(a.split(',')[1])) for a in x.split(' -> ')] for x in f.read().splitlines()]

grid = [['.' for _ in range(600)] for _ in range(200)]

height = 0

for rock in rocks:
	for i in range(1, len(rock)):
		height = max(height, rock[i][1])
		if rock[i][1] == rock[i - 1][1]:
			for x in range(rock[i - 1][0], rock[i][0] + (rock[i][0] - rock[i - 1][0]) // abs(rock[i][0] - rock[i - 1][0]), (rock[i][0] - rock[i - 1][0]) // abs(rock[i][0] - rock[i - 1][0])):
				grid[rock[i][1]][x] = '#'
		elif rock[i][0] == rock[i - 1][0]:
			for y in range(rock[i - 1][1], rock[i][1] + (rock[i][1] - rock[i - 1][1]) // abs(rock[i][1] - rock[i - 1][1]), (rock[i][1] - rock[i - 1][1]) // abs(rock[i][1] - rock[i - 1][1])):
				grid[y][rock[i][0]] = '#'
		
source = (500, 0)
grid[source[1]][source[0]] = '+'

units = 0

while True:
	at_rest = False
	units += 1
	sand = source
	while not at_rest:
		if grid[sand[1] + 1][sand[0]] not in ['o', '#']:
			sand = (sand[0], sand[1] + 1)
		elif grid[sand[1] + 1][sand[0] - 1] not in ['o', '#']:
			sand = (sand[0] - 1, sand[1] + 1)
		elif grid[sand[1] + 1][sand[0] + 1] not in ['o', '#']:
			sand = (sand[0] + 1, sand[1] + 1)
		else:
			at_rest = True
			grid[sand[1]][sand[0]] = 'o'
		if sand[1] == height:
			break
	if not at_rest:
		break

print(units - 1) # -1 because the source is counted as a unit