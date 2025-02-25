import sys
import copy
N = input().strip()
totalArray = [x for x in input().strip().split()]
equalIndex = []
just = -1
tally = {}
for i in range(int(N)):
    if tally.get(totalArray[i]) == None:
        tally[totalArray[i]] = 1
    else:
        tally[totalArray[i]] += 1
tally2 = copy.deepcopy(tally)
moos = set()
for i in range(1, len(totalArray)):
    if totalArray[i] == just:
        tally[totalArray[i]] -= 1
        continue
    just = -1

    if tally[totalArray[i]] > 1:
        tally[totalArray[i]] -= 1
        equalIndex.append(i)
        just = totalArray[i]

for i in range(len(equalIndex)):
    index = equalIndex[i]

    for j in range(index):
        if totalArray[j] == totalArray[index]:
            continue
        moos.add((totalArray[j], totalArray[index]))

print(len(moos))