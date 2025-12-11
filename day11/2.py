from util import *

s = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""".strip()
s = open("input.txt").read()

ans = 0
G = defaultdict(list)

for line in s.split("\n"):
    nodes = line.split(" ")
    node = nodes[0][:-1]
    G[node] = nodes[1:]


@cache
def dfs(node, dac, fft):
    if node == "out":
        return dac and fft
    n = 0
    for c in G[node]:
        n += dfs(c, dac or c == "dac", fft or c == "fft")
    return n


print(dfs("svr", False, False))
