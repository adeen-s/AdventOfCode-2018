import itertools

# Get input as integers inside a list n
with open("day-1/day-1-2-input.txt") as f:
    n = f.readlines()
n = [int(x.strip()) for x in n]

# Bruteforce solution. cycle through the inputs and check if frequency repeats
t = [0]
x = 0
for i in itertools.cycle(n):
    print(x) # Prints the current iteration
    x += 1
    t.append(t[-1] + i) 
    if len(t) != len(set(t)):
        print("answer = {}".format(t[-1]))
        a = False
        break

# Total Iterations for the input = 143548