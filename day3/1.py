from util import *

s = """
987654321111111
811111111111119
234234234234278
818181911112111
""".strip()
s = open("input.txt").read()

def joltage(x):
    m = 0
    for i in range(len(x)-1):
        for j in range(i + 1, len(x)):
            v = int(x[i] + x[j])
            if v > m:
                m = v
    return m

def joltage2(x):
    n = len(x)
    p = 12
    s = ""
    while (p > 0):
        v = max(x[:n-p+1])
        i = x.index(v)
        x = x[i+1:]
        n = len(x)
        s += str(v)
        p-=1
    print(s)
    return int(s)

ans = 0
for line in s.split():
    print(line)
    ans += joltage2(line)
print(ans)

