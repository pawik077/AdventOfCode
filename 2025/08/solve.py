import sys
from math import prod


# disjoint set union (union find) data structure
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.rank[rx] += self.rank[ry]
        self.components -= 1
        return True


def part1(data):
    points = [tuple(map(int, line.split(","))) for line in data]
    edges = []
    for i, x in enumerate(points):
        for j in range(i + 1, len(points)):
            y = points[j]
            dist = (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2
            edges.append({(i, j): dist})
    edges.sort(key=lambda e: list(e.values())[0])
    pairs = [
        (i, j)
        for edge in edges[: 10 if "-t" in sys.argv else 1000]
        for i, j in edge.keys()
    ]

    dsu = DSU(len(points))
    for i, j in pairs:
        dsu.union(i, j)
    sizes = {}
    for i in range(len(points)):
        root = dsu.find(i)
        sizes[root] = sizes.get(root, 0) + 1
    top = sorted(sizes.values(), reverse=True)[:3]
    return prod(top)


def part2(data):
    points = [tuple(map(int, line.split(","))) for line in data]
    edges = []
    for i, x in enumerate(points):
        for j in range(i + 1, len(points)):
            y = points[j]
            dist = (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2
            edges.append({(i, j): dist})
    edges.sort(key=lambda e: list(e.values())[0])
    pairs = [(i, j) for edge in edges for i, j in edge.keys()]

    dsu = DSU(len(points))
    last_pair = None
    for i, j in pairs:
        if dsu.union(i, j):
            last_pair = (i, j)
            if dsu.components == 1:
                break
    if last_pair:
        return points[last_pair[0]][0] * points[last_pair[1]][0]


if __name__ == "__main__":
    filename = "input" if "-t" not in sys.argv else "test"
    with open(filename) as f:
        data = f.read().splitlines()
    print(part1(data))
    print(part2(data))
