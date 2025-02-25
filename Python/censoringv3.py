import sys
sys.stdin = open("censor.in", "r")
sys.stdout = open("censor.out", "w")
mag = input().strip()
censor = input().strip()
while True:
    if mag.find(censor) == -1:
        break
    mag = mag.replace(censor, '')
    
print(mag)