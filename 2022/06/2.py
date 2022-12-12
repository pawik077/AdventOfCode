with open('input', 'r') as f:
	data = f.read()

for char in range(len(data)):
	if char < 14: continue
	temp = data[char-14:char]
	pass
	if len(temp) == len(set(temp)):
		print(char)
		break
