with open("day-2/day-2-1-input.txt") as f:
    l = f.readlines()
l = [x.strip() for x in l]
n = len(l[0])

for i in range (n):
    print(i)
    s = set()
    for x in l:
        if (x[:i] + x[i+1:]) in s:
            print(x[:i] + x[i+1:])
        s.add(x[:i] + x[i+1:])
