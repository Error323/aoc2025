from util import *

s = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
""".strip()
s = open("input.txt").read()

def invalid(x):
    s = str(x)
    m = 2
    n = len(s) // m
    while n > 0:
        if len(s) % m == 0:
            t = 0
            valid = True
            i = 1
            ss = s[:n]
            while i < m:
                if ss != s[i*n:(i+1)*n]:
                    valid = False
                    break
                #print(" ", ss, end='')
                i += 1

            if valid:
                print("!!", x, m)
                return True

        m += 1
        n = len(s) // m
    return False


ans = 0
for line in s.split(","):
    a, b = line.split("-")
    print(a, b)
    for x in range(int(a), int(b)+1):
        if invalid(x):
            ans += x
print(ans)
