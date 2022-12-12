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

sums.sort(reverse=True)
print(f'{sums[0] + sums[1] + sums[2]}')
