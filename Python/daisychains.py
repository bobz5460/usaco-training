import sys
n = int(input().strip())
flowers = [int(x) for x in input().strip().split()]
averageflower = 0
for i in range(n):
    for e in range(i, n):
        if e == i:
            averageflower+=1
            continue
        check = []
        average = 0
        for j in range(i, e+1):
            check.append(flowers[j])
            average+= flowers[j]
        average = average/len(check)
        for t in range(i, e+1):
            if check[t-i] == average:
                averageflower += 1
                break
print(averageflower)
