from util import *

s = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
""".strip()
s = open("input.txt").read()

ans = 0
G = defaultdict(list)

for line in s.split("\n"):
    nodes = line.split(" ")
    node = nodes[0][:-1]
    G[node] = nodes[1:]


def dfs(node):
    if node == "out":
        return 1
    n = 0
    for c in G[node]:
        n += dfs(c)
    return n


print(dfs("you"))
