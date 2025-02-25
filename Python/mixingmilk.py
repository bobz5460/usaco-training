import sys
sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")
inputs = []
for i in range(0,3):
    inputs.append(sys.stdin.readline().strip())
cap1, amount1 = inputs[0].split()
cap2, amount2 = inputs[1].split()
cap3, amount3 = inputs[2].split()
cap1, cap2, cap3, amount1, amount2, amount3 = int(cap1), int(cap2), int(cap3), int(amount1), int(amount2), int(amount3)
capacity = [cap1, cap2, cap3]
amount = [amount1, amount2, amount3]
for i in range(0, 100):
    currentIndex = i%3
    currentCap, currentAmount = capacity[currentIndex], amount[currentIndex]
    nextCap, nextAmount = capacity[(currentIndex+1)%3], amount[(currentIndex+1)%3]
    maxAmount = nextCap-nextAmount
    if currentAmount < maxAmount:
        amount[currentIndex] = 0
        amount[(currentIndex+1)%3] += currentAmount
    else:
        amount[currentIndex] = currentAmount - maxAmount
        amount[(currentIndex+1)%3] += maxAmount
for i in range(0,3):
    print(amount[i])
