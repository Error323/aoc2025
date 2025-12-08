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
        for c in line:
            if c == "+":
                o.append(add)
            elif c == "*":
                o.append(mul)
    else:
        for i, c in enumerate(line):
            d[i].append(c)

i = 0
l = []
for k in d:
    n = "".join(d[k])
    if len(n.strip()) == 0:
        print(o[i], l)
        ans += reduce(o[i], l)
        l = []
        i += 1
    else:
        print(n)
        l.append(int(n))
ans += reduce(o[i], l)


#for k in d:
#    if o[k] == "+":
#        ans += sum(d[k])
#    else:
#        x = 1
#        for v in d[k]:
#            x *= v
#        ans += x


print(ans)

