import sys
sys.stdin = open("shuffle.in", "r")
sys.stdout = open("shuffle.out", "w")
n = int(sys.stdin.readline().strip())
shuffleOrder = [int(x)-1 for x in sys.stdin.readline().strip().split()]
cowIDs = [x for x in sys.stdin.readline().strip().split()]
shuffled = [x for x in cowIDs]
toShuffle = [x for x in cowIDs]
for i in range(3):
    toShuffle = [x for x in shuffled]
    for e in range(n):
        #toShuffle = shuffled[shuffleOrder[e]]
        shuffled[e] = toShuffle[shuffleOrder[e]]
for i in range(n):
    print(shuffled[i])
