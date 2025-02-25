import sys
N = input().strip()
totalArray = [x for x in input().strip().split()]
equalIndex = []
just = -1
moos = set()
for i in range(1, len(totalArray)):
    if totalArray[i] == just:
        just = -1
        continue
    for j in range(i+1, len(totalArray)):
        if totalArray[i] == totalArray[j]:
            equalIndex.append((i,j))
            just = totalArray[i]
            break
for i in range(len(equalIndex)):
    mini = min(equalIndex[i])
    maxi = max(equalIndex[i])
    for j in range(mini):
        if totalArray[j] == totalArray[mini]:
            continue
        moos.add((totalArray[j], totalArray[mini], totalArray[maxi]))

print(len(moos))
