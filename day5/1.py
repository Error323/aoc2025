from util import *

s = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()
s = open("input.txt").read()

ans = 0
split = True
ranges = []
numbers = []
for line in s.split():
    if "-" in line:
        a, b = line.split("-")
        ranges.append((int(a), int(b)))
    else:
        x = int(line)
        numbers.append(x)


i = 0
ranges = sorted(ranges)
while i < len(ranges):
    a, b = ranges[i]
    i += 1
    while i < len(ranges):
        c, d = ranges[i]
        if c <= b:
            print(f"{a}-{b} {c}-{d} => {a}-{d}")
            b = max(b, d)
        else:
            break
        i += 1
    ans += b - a + 1


print(ans)

