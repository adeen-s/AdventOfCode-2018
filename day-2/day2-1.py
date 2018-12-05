from itertools import groupby

twos = 0
threes = 0

with open("day-2/day-2-1-input.txt") as f:
    l = f.readlines()
l = [x.strip() for x in l]
l = [sorted(list(x)) for x in l]

for i in l:
    group = [len(list(group)) for key, group in groupby(i)]
    if 2 in group:
        twos += 1
    if 3 in group:
        threes += 1
checksum = twos * threes
print(checksum)
