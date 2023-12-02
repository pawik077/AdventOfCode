import sys

def part1(data):
    sum = 0
    for line in data:
        digits = [int(x) for x in line if x.isdigit()]
        sum += digits[0] * 10 + digits[-1]
    return sum

def part2(data):
    nums = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    sum = 0
    for line in data:
        first = len(line)
        last = -1
        for x, i in nums.items():
            left = line.find(x)
            right = line.rfind(x)
            if left != -1:
                if left < first:
                    first = left
                    first_num = i
                if right > last:
                    last = right
                    last_num = i
        value = first_num * 10 + last_num
        sum += value
    return sum

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.readlines()
    print(part1(data))
    print(part2(data))