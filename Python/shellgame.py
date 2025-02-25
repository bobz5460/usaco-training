import sys
sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")
n = int(sys.stdin.readline())
turns = []
maximum = 0
for i in range(0,n):
    turns.append(sys.stdin.readline().strip())
maxpoints = 0
for i in range(0, 3):
    points = 0
    correctshell = i
    #thing = 
    
    for e in range(0, n):
        things = [int(x)-1 for x in turns[e].split()]
        if correctshell == things[0]:
            correctshell = things[1]
        elif correctshell == things[1]:
            correctshell = things[0]
        guess = things[2]
        if guess == correctshell:
            points +=1
    if points>maxpoints:
        maxpoints = points
print(maxpoints)