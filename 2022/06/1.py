with open('input', 'r') as f:
	data = f.read()

for char in range(len(data)):
	if char < 4: continue
	temp = data[char-4:char]
	pass
	if len(temp) == len(set(temp)):
		print(char)
		break
