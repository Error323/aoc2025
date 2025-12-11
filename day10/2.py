from util import *
import z3


s = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".strip()
s = open("input.txt").read()

ans = 0

machines = []
for line in s.split("\n"):
    if len(line) > 0:
        row = line.split(" ")
        levels = ints(row[-1])
        buttons = [ints(x) for x in row[1:-1]]
        machines.append((levels, buttons))


for levels, buttons in machines:
    z = z3.Optimize()
    zvars = z3.Ints(f"n{i}" for i in range(len(buttons)))
    for b in zvars:
        z.add(b >= 0)

    for i, level in enumerate(levels):
        eq = 0
        for j, button in enumerate(buttons):
            if i in button:
                eq += zvars[j]
        z.add(eq == level)

    z.minimize(sum(zvars))
    z.check()
    ans += z.model().eval(sum(zvars)).as_long()

print(ans)

