from functools import cmp_to_key

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

packets.append([[2]])
packets.append([[6]])
packets.sort(key=cmp_to_key(compare_all))

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))