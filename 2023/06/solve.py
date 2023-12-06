import sys

def part1(data):
    data = [[int(x) for x in y] for y in [z.split()[1:] for z in data]]
    data = list(zip(data[0], data[1]))
    prod = 1
    for time, record_distance in data:
        beats = 0
        for speed in range(0, time + 1):
            if speed * (time - speed) > record_distance:
                beats += 1
        prod *= beats
    return prod

def part2(data):
    data = [int(x.replace(' ', '').split(':')[1]) for x in data]
    time = data[0]
    record_distance = data[1]
    distance = 0
    min_speed = 0
    max_speed = time
    while distance < record_distance:
        min_speed += 1
        distance = min_speed * (time - min_speed)
    distance = 0
    while distance < record_distance:
        max_speed -= 1
        distance = max_speed * (time - max_speed)    
    return max_speed - min_speed + 1

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))