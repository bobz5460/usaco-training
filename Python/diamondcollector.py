import sys
sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")
n, k = sys.stdin.readline().strip().split()
n, k = int(n), int(k)
sizes = []
minremoved = 99999999999
for i in range(n):
    sizes.append(int(sys.stdin.readline().strip()))
for i in range(n):
    removed = 0
    minsize = sizes[i]
    maxsize = minsize + k
    for e in range(n):
        if sizes[e] >= minsize and sizes[e] <= maxsize:
            continue
        else:
            removed += 1
    minremoved = min(minremoved, removed)
print(n-minremoved)
