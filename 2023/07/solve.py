import sys
from collections import Counter

def get_type(hand):
    # -4,-3,-2,-1,0,1,2,4: hand type,
    # it's kinda complicated, recommend to draw it on paper
    return max(Counter(hand).values()) - len(set(hand))

# same as above, but adding jokers to the most common card
def get_type_with_jokers(hand):
    c = Counter(hand)
    if 'J' in c:
        jokers = c.pop('J')
        if c: c[max(c, key=c.get)] += jokers
        else: c['J'] = jokers
    return max(c.values()) - len(c.values())

def part1(data):
    hands = [(hand, int(bid)) for (hand, bid) in [line.split() for line in data]]
    # hands = sorted([(hand type, values of cards, bid)])
    hands = sorted([(get_type(hand), *map('23456789TJQKA'.index, hand), bid) for (hand, bid) in hands])
    return sum([hands[i][-1] * (i + 1) for i in range(len(hands))])


def part2(data):
    hands = [(hand, int(bid)) for (hand, bid) in [line.split() for line in data]]
    hands = sorted([(get_type_with_jokers(hand), *map('J23456789TQKA'.index, hand), bid) for (hand, bid) in hands])
    return sum([hands[i][-1] * (i + 1) for i in range(len(hands))])

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))