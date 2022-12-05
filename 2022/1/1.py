with open('input', 'r') as f:
	data = f.read().splitlines()
elves = []
foods = []
for i in data:
	if i == '':
		elves.append(foods)
		foods = []
		continue
	foods.append(int(i))
elves.append(foods)

sums = []

for i in elves:
	sums.append(sum(i))

print(f'{sums.index(max(sums))} {max(sums)}')