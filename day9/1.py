from util import *

s = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip()
s = open("input.txt").read()

ans = 0
def area(p1, p2):
    return abs(p1[0]-p2[0] + 1)*abs(p1[1]-p2[1] + 1)

points = []
for line in s.split():
    x, y = ints(line)
    points.append((x, y))

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        a = area(points[i], points[j])
        ans = max(a, ans)
        print(points[i], points[j], ans)
print(ans)

