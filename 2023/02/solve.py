import sys

def part1(data):
    sum = 0
    for game in data:
        possible = True
        id = int(game.split(':')[0].split(' ')[1])
        rounds = game.split(': ')[1].split('; ')
        for round in rounds:
            color_strings = [x.split(' ') for x in round.split(', ')]
            colors = {'red': 0, 'green': 0, 'blue': 0}
            for color in color_strings:
                colors[color[1]] = int(color[0])
            if colors['red'] > 12 or colors['green'] > 13 or colors['blue'] > 14:
                possible = False
                break
        if possible:
            sum += id
    return sum

def part2(data):
    sum = 0
    for game in data:
        rounds = game.split(': ')[1].split('; ')
        max_colors = {'red': 0, 'green': 0, 'blue': 0}
        for round in rounds:
            color_strings = [x.split(' ') for x in round.split(', ')]
            colors = {'red': 0, 'green': 0, 'blue': 0}
            for color in color_strings:
                colors[color[1]] = int(color[0])
            if colors['red'] > max_colors['red'] and colors['red'] != 0:
                max_colors['red'] = colors['red']
            if colors['green'] > max_colors['green'] and colors['green'] != 0:
                max_colors['green'] = colors['green']
            if colors['blue'] > max_colors['blue'] and colors['blue'] != 0:
                max_colors['blue'] = colors['blue']
        sum += max_colors['red'] * max_colors['green'] * max_colors['blue']
    return sum

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))