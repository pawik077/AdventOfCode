import sys

def part1(data):
    data = [int(x) for x in data]
    disk = []
    id = 0
    for i in range(len(data)):
        if i % 2 == 0:
            for i in range(data[i]):
                disk.append(id)
            id += 1
        else:
            for i in range(data[i]):
                disk.append('.')
    for i in range(len(disk) - 1, 0, -1):
        empty = disk.index('.')
        if empty < i:
            disk[empty] = disk[i]
            disk[i] = '.'
    disk = disk[:disk.index('.')]
    return sum([x * i for i, x in enumerate(disk)])

def part2(data):
    data = [int(x) for x in data]
    disk = []
    id = 0
    for i in range(len(data)):
        if i % 2 == 0:
            for i in range(data[i]):
                disk.append(id)
            id += 1
        else:
            for i in range(data[i]):
                disk.append('.')
    i = len(disk) - 1
    j = 0
    while i > 0:
        if disk[i] == '.':
            i -= 1
            continue
        first_byte = disk.index(disk[i])
        file_size = disk.count(disk[i])
        j = 0
        while j < i:
            if disk[j] == '.':
                space_size = 0
                while j + space_size < i and disk[j + space_size] == '.':
                    space_size += 1
                if space_size >= file_size:
                    disk[j:j + file_size] = [disk[i]] * file_size
                    disk[first_byte:first_byte + file_size] = ['.'] * file_size
                    break
            j += 1
        i = first_byte - 1
    return sum([x * i for i, x in enumerate(disk) if x != '.']) 

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().strip()
    print(part1(data))
    print(part2(data))
    