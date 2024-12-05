import sys

def check_update(update, rules):
    for rule in rules:
        if rule[0] not in update or rule[1] not in update: continue
        if update.index(rule[0]) > update.index(rule[1]):
            return False
    return True

def fix_update(update, rules):
    while not check_update(update, rules):
        if not check_update(update, rules):
            for rule in rules:
                if rule[0] not in update or rule[1] not in update: continue
                if update.index(rule[0]) > update.index(rule[1]):
                    update[update.index(rule[0])], update[update.index(rule[1])] = update[update.index(rule[1])], update[update.index(rule[0])]
    return update

def part1(data):
    rules = []
    updates = []
    total = 0
    for line in data:
        if line == '': continue
        if '|' in line:
            rules.append(tuple([int(x) for x in line.split('|')]))
        else:
            updates.append([int(x) for x in line.split(',')])
    for update in updates:
        if check_update(update, rules):
            total += update[len(update)//2]
    return total

def part2(data):
    rules = []
    updates = []
    incorrect_updates = []
    total = 0
    for line in data:
        if line == '': continue
        if '|' in line:
            rules.append(tuple([int(x) for x in line.split('|')]))
        else:
            updates.append([int(x) for x in line.split(',')])
    for update in updates:
        if not check_update(update, rules):
            incorrect_updates.append(update)
    for update in incorrect_updates:
        update = fix_update(update, rules)
    for update in incorrect_updates:
        total += update[len(update)//2]
    return total

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))
    