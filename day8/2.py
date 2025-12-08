from util import *

s = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".strip()
s = open("input.txt").read()

ans = 1

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

jb = []
for line in s.split():
    x,y,z = line.split(",")
    jb.append((int(x), int(y), int(z)))

nodes = defaultdict(dict)
distances = []

for i in range(len(jb)):
    jb1 = jb[i]
    for j in range(i + 1, len(jb)):
        jb2 = jb[j]
        distances.append((distance(jb1, jb2), jb1, jb2))


distances = sorted(distances)
circuits = []

# a, b [[a, b]]
# d, e [[a, b], [d, e]]
# b, e [[a, b, d, e]]

last = (None, None)
for _, j1, j2 in distances:
    merge = []
    already = False
    for i, c in enumerate(circuits):
        if j1 in c and j2 in c:
            already = True
            break

        if j1 in c:
            merge.append((i, j2))

        if j2 in c:
            merge.append((i, j1))

    if already:
        continue

    if len(merge) == 0:
        c = set()
        c.add(j1)
        c.add(j2)
        circuits.append(c)
    elif len(merge) == 1:
        i, ji = merge[0]
        circuits[i].add(ji)
        last = (j1, j2)
    else:
        i, _ = merge[0]
        j, _ = merge[1]
        circuits[i] |= circuits[j]
        circuits.pop(j)
        last = (j1, j2)

print(last[0][0] * last[1][0])

