import sys
thing = {}
sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")
john = sys.stdin.readline()
bessie = sys.stdin.readline()
johnstart, johnend = john.split(" ")
bessiestart, bessieend = bessie.split(" ")
for i in range(int(johnstart), int(johnend)):
    thing[i] = i
for i in range(int(bessiestart), int(bessieend)):
    thing[i] = i
print(len(thing))
