import sys
sys.stdin = open("cbarn.in", "r")
sys.stdout = open("cbarn.out", "w")
n = sys.stdin.readline().strip()
n = int(n)
_ = sys.stdin.readlines()
rooms = [int(x.strip()) for x in _]
minDistance = None
for i in range(0,n):
    distance = 0
    #openedDoor = rooms[i]
    for e in range(i,n+i):
        _ = e%n
        distance += (rooms[_])*(e-i)
    if minDistance == None or distance < minDistance:
        minDistance = distance
print(minDistance)