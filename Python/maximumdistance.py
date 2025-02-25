import sys
n = int(input())
xList = [int(x) for x in input().strip().split()]
yList = [int(y) for y in input().strip().split()]
maxdistance = 0
for thing in range(n):
    for thing2 in range(n):
        x1,x2,y1,y2 = xList[thing], xList[thing2], yList[thing], yList[thing2]
        maxdistance = max(maxdistance, (((x2-x1)^2)+((y2-y1)^2)))
print(maxdistance)
