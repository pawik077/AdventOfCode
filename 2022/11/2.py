import math

with open('input', 'r') as f:
	data = f.read().splitlines()

class Monkey:
	def __init__(self, items, operation, divisor, target_if_true, target_if_false):
		self.items = items
		self.operation = operation
		self.divisor = divisor
		self.target_if_true = target_if_true
		self.target_if_false = target_if_false
		self.inspections = 0

monkeys = []

for i in range(len(data)):
	if data[i].startswith('Monkey'):
		i += 1
		items = [int(x) for x in data[i].replace(',', '').split(' ')[4:]]
		i += 1
		operation = data[i][19:]
		i += 1
		divisor = int(data[i][21:])
		i += 1
		target_if_true = int(data[i][29:])
		i += 1
		target_if_false = int(data[i][30:])
		i += 2
		monkeys.append(Monkey(items, operation, divisor, target_if_true, target_if_false))

divisor_product = math.prod([x.divisor for x in monkeys]) # common divisor

for round in range(0, 10000):
	for monkey in monkeys:
		old_items = monkey.items.copy()
		for item in old_items:
			old = item
			new = eval(monkey.operation)
			new %= divisor_product # modulo common divisor, to keep worry levels manageable
			if new % monkey.divisor == 0:
				monkeys[monkey.target_if_true].items.append(new)
			else:
				monkeys[monkey.target_if_false].items.append(new)
			monkey.items.remove(old)
			monkey.inspections += 1

inspections = sorted([x.inspections for x in monkeys], reverse=True)
print(inspections[0] * inspections[1])