from util import *

s = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".strip()
s = open("input.txt").read()

ans = 0

machines = []
for line in s.split("\n"):
    row = line.split(" ")
    lights = 0
    for p, c in enumerate(row[0][1:-1].strip()):
        if c == "#":
            lights ^= 1 << p
    buttons = [ints(x) for x in row[1:-1]]
    machines.append((lights, buttons))

def push(lights, button):
    for b in button:
        lights ^= 1 << b
    return lights
    


for lights, buttons in machines:
    def children(node):
        c = []
        for b in buttons:
            c.append((1, push(node, b)))
        return c

    score, path = dijkstra(0, lights, children)
    ans += score

print(ans)

