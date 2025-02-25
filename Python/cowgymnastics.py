import sys
sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")
K, N = sys.stdin.readline().strip().split()
K, N = int(K), int(N)
ranks = []
valid = 0
for i in range(K):
    ranks.append([int(x) for x in sys.stdin.readline().strip().split()])
for i in range(N):
    for j in range(i, N):
        if i == j:
            continue
        a1 = ranks[0][i] #cow number
        b1 = ranks[0][j] #cow number
        consistant = True
        for e in range(1,K):
            a2 = ranks[e].index(a1)
            b2 = ranks[e].index(b1)
            if a2 < b2:
                continue
            else:
                consistant = False
                break
        if consistant:
            valid +=1
print(valid)