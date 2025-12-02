from util import *

s = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".strip()
s = open("input.txt").read()

pos = 50
ans = 0
for line in s.split():
    p = pos
    n = int(line[1:])

    if n > 100:
        ans += n // 100
        n %= 100

    if line[0] == "L":
        pos -= n
        if pos <= 0 and p != 0:
            ans += 1
    else:
        pos += n
        if pos >= 100 and p != 0:
            ans += 1

    pos %= 100
print(ans)

