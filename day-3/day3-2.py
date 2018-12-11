import re

with open("day-3/day-3-2-input.txt") as f:
    n = f.readlines()
n = [x.strip() for x in n]
n = [re.findall(r'-?\d+', i) for i in n]
n = [i[1:] for i in n]
n = [[int(x) for x in m] for m in n]

fabric = [[0 for x in range(1000)] for y in range(1000)]
ids = [x + 1 for x in range(len(n))]

for id,i in enumerate(n):
    id += 1
    for x in range(i[1], i[1] + i[3]):
        for y in range(i[0], i[0] + i[2]):
            if(fabric[x][y] == 0):
                fabric[x][y] = id
            else:
                if fabric[x][y] in ids:
                    ids.remove(fabric[x][y])
                if id in ids:
                    ids.remove(id)
# for i in range(1000):
#     for j in range(1000):
#         print(fabric[i][j], end=' ')
#     print()

print("ans = {}".format(ids))