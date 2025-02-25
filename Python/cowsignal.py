import sys
sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")
dimensions = [int(x) for x in sys.stdin.readline().split()]
length, width, multiplier = dimensions[0], dimensions[1], dimensions[2]
original = []
modified = []
for i in range(0,length):
    original.append(sys.stdin.readline().strip())
for i in range(0, length):
    line = original[i]
    for e in range(width*multiplier):
        if e%width == 0 and not (i==0 and e==0):
            print('')
        print(line[e%width]*multiplier, end='')