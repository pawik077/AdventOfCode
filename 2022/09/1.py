with open('input', 'r') as f:
	data = f.readlines()

head = (0, 0)
tail = (0, 0)
head_old = (0, 0)
tails = [tail]

for line in data:
	for i in range(int(line[2:])):
		head_old = head
		match line[0]:
			case 'R': 
				head = (head[0] + 1, head[1])
			case 'L':
				head = (head[0] - 1, head[1])
			case 'U':
				head = (head[0], head[1] + 1)
			case 'D':
				head = (head[0], head[1] - 1)
		if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
			tail = head_old
			if tail not in tails:
				tails.append(tail)

print(len(tails))