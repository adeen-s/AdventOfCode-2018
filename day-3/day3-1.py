import re

with open("day-3/day-3-1-input.txt") as f:
    n = f.readlines()
n = [x.strip() for x in n]
n = [re.findall(r'-?\d+', i) for i in n]
n = [i[1:] for i in n]
n = [[int(x) for x in m] for m in n]

fabric = [[0 for x in range(1000)] for y in range(1000)]

for i in n:
    for x in range(i[1], i[1] + i[3]):
        for y in range(i[0], i[0] + i[2]):
            fabric[x][y] += 1

ans = 0

for x in range(1000):
    for y in range(1000):
        if fabric[x][y] >= 2:
            ans += 1

print(ans)