from util import *
from PIL import Image, ImageDraw

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
points = []


xmin, xmax = math.inf, 0
ymin, ymax = math.inf, 0
for line in s.split():
    x, y = ints(line)
    xmin = min(xmin, x)
    ymin = min(ymin, y)
    xmax = max(xmax, x)
    ymax = max(ymax, y)
    points.append((x, y))

RATIO = (xmax - xmin) / (ymax - ymin)
SIZEY = 1024
SIZEX = SIZEY * RATIO
xscale = SIZEX / (xmax - xmin)
yscale = SIZEY / (ymax - ymin)
im = Image.new("RGBA", (math.ceil(SIZEX), math.ceil(SIZEY)), (255, 255, 255, 255))
draw = ImageDraw.Draw(im)

def scale(x, y):
    return math.floor(xscale * (x - xmin)), math.floor(yscale * (y - ymin))

b = 0
r = 255
for p1, p2 in zip(points[:-1], points[1:]):
    draw.line([scale(*p1), scale(*p2)], fill=(round(r),10,round(b)), width=1)
    b += 255/(len(points)-1)
    r -= 255/(len(points)-1)
draw.line([scale(*points[-1]), scale(*points[0])], fill=(round(r),10,round(b)), width=1)

def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

p1 = points[len(points)//2]
i = 0
p2 = points[i]
while p1[0] < p2[0]:
    i += 1
    p2 = points[i]
p2 = points[i-1]
i = len(points)//4
p3 = points[i]
while p2[1] < p3[1]:
    i += 1
    p3 = points[i]
p3 = points[i+1]
ans=area(p1,p3)

best = [p3[0], p1[1], p1[0], p3[1]]
draw.rectangle([scale(*best[:2]),scale(*best[2:])], outline=(200,200,200))
        
im.show()

"""
def inpoly(p1, p2):
    p3 = (p2[0], p1[1])
    p4 = (p1[0], p2[1])
    return p3 in points or p4 in points


for i, p1 in enumerate(points):
    for p2 in points[i+1:]:
        if inpoly(p1, p2):
            a = area(p1, p2)
            print(p1, p2, a)
            ans = max(a, ans)
"""

print(ans)
