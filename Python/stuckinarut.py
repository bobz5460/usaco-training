import sys
n = int(input().strip())
directions = []
cords = []
grassEaten = [1]*n
alive = [True]*n
eatenCells = set()
for i in range(n):
    thing = input().strip().split()
    directions.append(thing[0])
    cords.append([int(thing[1]), int(thing[2])])
    eatenCells.add((int(thing[1]), int(thing[2])))
while True:
    eaten_thishour = set()
    for i in range(n):
        if not alive[i]:
            continue
        next_cell = (cords[i][0] + 1, cords[i][1]) if directions[i] == 'E' else (cords[i][0], cords[i][1] + 1)
        cords[i] = (next_cell[0], next_cell[1])
        if next_cell in eatenCells:
            alive[i] = False
        else:
            grassEaten[i] += 1
            eaten_thishour.add(next_cell)
    eatenCells = eatenCells.union(eaten_thishour)

# check infinity
    for i in range(n):
        if not alive[i]:
            continue
        thing = True
        for j in range(n):
            if j == i or not alive[j] or directions[j] == directions[i]:
                continue
            j_thing = cords[j][1] < cords[i][1] if directions[i] == 'N' else cords[j][0] < cords[i][0]
            if not j_thing:
                thing = False
                break
        if thing:
            alive[i] = False
            grassEaten[i] = 'Infinity'
  
    if alive == [False]*n:
        break
for i in grassEaten:
    print(i)     