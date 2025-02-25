import sys
sys.stdin = open("pails.in", "r")
sys.stdout = open("pails.out", "w")
x, y, m = sys.stdin.readline().strip().split()
x, y, m = int(x), int(y), int(m)
maxAmount = 0
for i in range((m//x)+1):
    for e in range((m//y)+1):
        amount = (i*x)+(e*y)
        if amount <= m:
            maxAmount = max(maxAmount, amount)
print(maxAmount)