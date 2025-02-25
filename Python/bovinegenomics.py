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
    valid = {'A', 'C', 'G', 'T'}
    genome = True
    for j in range(N):
        valid.discard(spotty[j][i])
    for j in range(N):
        if plain[j][i] in valid:
            continue
        else:
            genome = False
            break
    if genome:
        count +=1
print(count)