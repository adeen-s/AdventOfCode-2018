with open("day-1-1-input.txt") as f:
    n = f.readlines()
n = [int(x.strip()) for x in n]

print(sum(n))