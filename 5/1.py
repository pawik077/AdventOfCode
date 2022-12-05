import re
with open('input', 'r') as f:
	data = f.read().splitlines()

stacks_alpha = []
for i in range(int(data[data.index('') - 1][-2])):
	stacks_alpha.append([])

for line in data:
	crates = re.findall(r'(\[[A-Z]\]|    )', line)
	if crates == []: break
	for stack in range(len(stacks_alpha)):
		stacks_alpha[stack].append(crates[stack])

stacks = []
for stack in stacks_alpha:
	stack = [x for x in stack if x != '    ']
	stack.reverse()
	stacks.append(stack)

for line in data:
	if not line.startswith('move'): continue
	line = line.split(' ')
	number = int(line[1])
	source = int(line[3]) - 1
	dest = int(line[5]) - 1
	for i in range(number):
		stacks[dest].append(stacks[source].pop())

for i in range(len(stacks)):
	print('Stack', i + 1, ':', end=' ')
	for crate in stacks[i]:
		print(crate, end=' ')
	print()
