with open('input', 'r') as f:
	data = f.read().splitlines()
subsets = 0
for line in data:
	first, second = line.split(',')
	first = range(int(first.split('-')[0]), int(first.split('-')[1]) + 1)
	second = range(int(second.split('-')[0]), int(second.split('-')[1]) + 1)
	if(any(x in second for x in first) or any(x in first for x in second)):
		subsets += 1
print(subsets)