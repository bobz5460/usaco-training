import sys
T = int(input().strip())
N, A, B = input().strip().split()
N, A, B = int(N), int(A), int(B)
array = []
states = [['O']*N]*N

def changeState(x, y, changeTo):
    beforeState = states[x][y]
    if beforeState == 'O':
        states[x][y] = changeTo
        return True
    elif beforeState == 'A':
        if changeTo == 'A':
            return True
        return False
    elif beforeState == 'B':
        if changeTo == 'D' or changeTo == 'B':
            return True
        return False
    elif beforeState == 'C':
        if changeTo == 'D' or changeTo == 'C':
            return True
        return False
    elif beforeState == 'D':
        if changeTo == 'B' or changeTo == 'C':
            states[x][y] = changeTo
            return True
        return False

for i in range(N):
    array.append(input().strip().split())

for x in range(N):
    for y in range(N):
        if array[x][y] == 'W':
            if changeState(x, y, 'A'):
                continue
            break