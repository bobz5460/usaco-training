import sys
import copy
N = int(input().strip())
cowOrder = input().strip().split()
docOrder = input().strip().split()
output = [0]*(N+1)
j=0
k=0
cowOrderCopy = copy.deepcopy(cowOrder)
count = 0
for m in range(N):
    if docOrder[m] == cowOrderCopy[m]:
        count += 1
output[count] += N

for j in range(N):
    for k in range(j+1,N):
        cowOrderCopy = copy.deepcopy(cowOrder)
        cowOrderCopy[j:k+1] = reversed(cowOrderCopy[j:k+1])
        count = 0
        for m in range(N):
            if docOrder[m] == cowOrderCopy[m]:
                count += 1
        output[count] += 1
for i in range(len(output)):
    print(output[i])