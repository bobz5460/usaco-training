import sys
sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")
cross = input().strip()
index = 0
while True:
    if index < 0:
        index = 0
    current = cross[index]
    next = cross[index+1]
    
    if current == next:
        cross = cross[:index] + cross[index+2:]
        index -= 1
    else:
        index +=1
    if index == len(cross)-1:
        break
index = 0
pairs = set()
while True:
    if index+1 >= len(cross):
        break
    current = cross[index]
    temp = set()
    for i in range(index+1,len(cross)):
        if i == len(cross):
            break
        if current == cross[i]:
            for j in temp:
                pairs.add((current, j))
                pairs.add((j, current))
            break
        if cross[i] in temp:
            temp.remove(cross[i])
        else:
            temp.add(cross[i])
    index +=1
print(len(pairs)//2)

