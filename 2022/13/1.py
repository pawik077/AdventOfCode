def compare(v1, v2) -> int:
	if isinstance(v1, int) and isinstance(v2, int):
		return (v1 - v2) // abs(v1 - v2) if v1 != v2 else 0
	if isinstance(v1, list) and isinstance(v2, list):
		if len(v1) == 0 and len(v2) == 0:
			return 0
		elif len(v1) == 0:
			return -1
		elif len(v2) == 0:
			return 1
		else:
			return compare_all(v1, v2)
	if isinstance(v1, int) and isinstance(v2, list):
		return compare([v1], v2)
	if isinstance(v1, list) and isinstance(v2, int):
		return compare(v1, [v2])

def compare_all(v1, v2):
	for i in range(min(len(v1), len(v2))):
		result = compare(v1[i], v2[i])
		if result != 0:
			return result
	if len(v1) < len(v2):
		return -1
	elif len(v1) == len(v2):
		return 0
	elif len(v1) > len(v2):
		return 1


with open('input', 'r') as f:
	packets = [eval(x) for x in f.read().splitlines() if x != '']

correct = []

for i in range(1,len(packets), 2):
	correct.append(compare_all(packets[i - 1], packets[i]))
	pass

for i in range(len(correct)):
	print(f"chunk {i + 1}: {correct[i]}")

sum = 0
for i in range(len(correct)):
	if correct[i] < 1:
		sum += i + 1

print(sum)