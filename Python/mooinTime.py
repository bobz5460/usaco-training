import sys
N = input().strip()
totalArray = [x for x in input().strip().split()]
moos = set()
for i in range(len(totalArray)):
    for j in range(i+1, len(totalArray)):
        for k in range(j+1, len(totalArray)):
            if totalArray[j]!=totalArray[k]:
                continue
            if totalArray[j] == totalArray[i]:
                continue
            moos.add((totalArray[i],totalArray[j],totalArray[k]))
print(len(moos))
