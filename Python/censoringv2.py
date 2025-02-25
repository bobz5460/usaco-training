import sys
sys.stdin = open("censor.in", "r")
sys.stdout = open("censor.out", "w")
mag = input().strip()
censor = input().strip()
index = 0
while True:
    if index < 0:
        index = 0
    thing = mag.find(censor, index)
    if thing != -1:
        mag = mag[:thing] + mag[thing+len(censor):]
        index = thing-len(censor)+1
    else:
        break
print(mag)