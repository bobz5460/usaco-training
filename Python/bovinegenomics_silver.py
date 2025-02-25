import sys
sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")
N, M = input().strip().split()
N, M = int(N), int(M)
spotty = []
plain = []
count = 0
for i in range(N):
    spotty.append(input().strip())
for i in range(N):
    plain.append(input().strip())
for i in range(M):
    for j in range(i+1, M):
        for t in range(j+1, M):
            spots = set()
            for k in range(N):
                things = (spotty[k][i], spotty[k][j], spotty[k][t])
                spots.add(things)
            broke = False
            for e in range(N):
                things = (plain[e][i], plain[e][j], plain[e][t])
                if things in spots:
                    broke = True
                    break
                else:
                    continue
            if not broke:
                count+=1
print(count)