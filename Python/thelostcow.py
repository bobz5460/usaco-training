import sys
sys.stdin = open("lostcow.in", "r")
sys.stdout = open("lostcow.out", "w")
x, y = sys.stdin.readline().strip().split()
x, y = int(x), int(y)
add = 1
direction = '+'
distance = 0
goto = x
while True:
    if direction == '+':
        distance += abs(goto-(x+add))
        goto = x+add
        add *=2
        direction = '-'
        if goto >= y and x<y:
            distance-=goto-y
            break

    else:
        distance += abs(goto-(x-add))
        goto = x-add
        direction = '+'
        add*=2
        if goto <= y and x>y:
            distance -= y-goto
            break
print(distance)