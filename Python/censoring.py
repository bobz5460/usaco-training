import sys
sys.stdin = open("censor.in", "r")
sys.stdout = open("censor.out", "w")
magazine = sys.stdin.readline().strip()
censor = sys.stdin.readline().strip()
index = -1
while True:
    index+=1
    if index < 0:
         index = 0
    for i in range(index, len(magazine)- len(censor)):
        counter = -1
        for e in range(i, i+len(censor)):
            counter +=1
            if censor[counter] != magazine[e]:
                break
        if censor[counter] != magazine[e]:
                continue
        for _ in range(len(censor)):
            magazine = magazine[:i] + magazine[i+1:]
        index -= len(censor)
    if i == len(magazine)- len(censor)-1:
        break
print(magazine)