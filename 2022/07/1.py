class dir:
	def __init__(self, name, parent):
		self.name = name
		self.parent = parent
		self.children = []

	def add_child(self, child):
		self.children.append(child)

	def get_path(self):
		if self.parent:
			return (self.parent.get_path() if self.parent.name != '/' else '') + '/' + self.name
		else:
			return self.name

	def __repr__(self):
		return self.name

class file:
	def __init__(self, name, parent, size):
		self.name = name
		self.parent = parent
		self.size = size

	def get_path(self):
		p = self.parent.get_path()
		n = self.parent.name
		pass
		return (self.parent.get_path() if self.parent.name != '/' else '')  + '/' + self.name

	def __repr__(self):
		return self.name

def calculate_sizes(dir):
	size = 0
	for child in dir.children:
		if isinstance(child, file):
			size += int(child.size)
		else:
			size += calculate_sizes(child)
	return size

with open('input', 'r') as f:
	lines = f.read().splitlines()

fs = {'/': dir('/', None)}
cwd = None
for line in lines:
	if line.startswith('$'):
		if line[2:4] == 'cd':
			if line[5:] == '/':
				cwd = fs['/']
				continue
			if line[5:] == '..':
				cwd = fs[cwd.parent.get_path()]
				continue
			cwd = fs[cwd.get_path() + ('/' if cwd.name != '/' else '') + line[5:]]
		elif line[2:4] == 'ls':
			continue
	elif line.startswith('dir'):
		name = line[4:]
		fs[cwd.get_path() + ('/' if cwd.name != '/' else '') + name] = dir(name, cwd)
		fs[cwd.get_path()].add_child(fs[cwd.get_path() + ('/' if cwd.name != '/' else '') + name])
	else:
		size, name = line.split()
		fs[cwd.get_path() + ('/' if cwd.name != '/' else '') + name] = file(name, cwd, size)
		fs[cwd.get_path()].add_child(fs[cwd.get_path() + ('/' if cwd.name != '/' else '') + name])

sum = 0
for i in fs:
	if isinstance(fs[i], dir):
		size = calculate_sizes(fs[i])
		if size < 100000:
			sum += size


print(sum)