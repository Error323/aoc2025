from util import *

s = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
""".strip()
s = open("input.txt").read()

ans = 0
d = defaultdict(list)
o = []
for line in s.split("\n"):
    if len(line) <= 0:
        continue
    if line[0] == "+" or line[0] == "*":
        for op in line.split():
            o.append(op)
    else:
        l = ints(line)
        for i, x in enumerate(l):
            d[i].append(x)

for k in d:
    if o[k] == "+":
        ans += sum(d[k])
    else:
        x = 1
        for v in d[k]:
            x *= v
        ans += x


print(ans)

