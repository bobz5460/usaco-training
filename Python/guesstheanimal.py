import sys
sys.stdin = open("guess.in", "r")
sys.stdout = open("guess.out", "w")
animals = []
char = []
N = int(input().strip())
for i in range(N):
    temp = input().strip().split()
    animals.append(temp[0])
    char.append(set(temp[2:]))
count = 0
for i in range(N):
    for j in range(i,N):
        if i == j:
            continue
        count = max(count, len(char[i]&char[j])+1)
print(count)