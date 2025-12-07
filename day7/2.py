from util import *
import numpy as np

s = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip()
s = open("input.txt").read()

g, n, m = grid_from_string(s)
ans = 0
"""
for i in range(n):
    for j in range(m):
        if g[i][j] == "S":
            g[i+1][j] = "|"
        elif g[i][j] == "^":
            g[i][j-1] = "|"
            g[i][j+1] = "|"
        elif g[i][j] == "." and i > 0 and g[i-1][j] == "|":
            g[i][j] = "|"

for i in range(n):
    for j in range(m):
        if g[i][j] == "^" and g[i-1][j] == "|":
            ans += 1
        print(g[i][j], end='')
    print()
"""

@cache
def dfs(depth, n, m):
    if depth == n:
        return 1

    total = 0
    if g[depth][m] == "^":
        total += dfs(depth + 1, n, m - 1)
        total += dfs(depth + 1, n, m + 1)
    elif g[depth][m] == ".":
        total += dfs(depth + 1, n, m)
    return total



print(dfs(1, n, m // 2))

