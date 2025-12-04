from util import *

s = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()
s = open("input.txt").read()

ans = 0
g, m, n = grid_from_string(s)
while True:
    pans = ans
    for y in range(n):
        for x in range(m):
            if g[y][x] != "@":
                continue
            count = 0
            for i, j in C8:
                if i+y >= 0 and i+y < n and x+j >= 0 and x+j < m:
                    count += g[y+i][x+j] == "@"
            if count < 4:
                ans += 1
                g[y][x] = "x"
    if pans == ans:
        break
print(ans)


