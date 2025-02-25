import sys
eatenCells = set()
class Cow:
    
    def __init__(self, x, y, d):
        self.x = int(x)
        self.y = int(y)
        self.d = d
        self.alive = True
        self.eaten = 0
    
    def cord(self):
        return (self.x, self.y)
    def maybeStop(self):
        if self.alive and self.cord() in eatenCells:
            self.alive = False
    def move(self):
        if self.alive:
            if self.d == 'N':
                self.y += 1
            else:
                self.x += 1
    def eat(self):
        if self.alive:
            self.eaten += 1
            return True
        return False
    def outOfWay(self, cow):
        if (not self.alive or not cow.alive) or (self.d == cow.d):
            return True        
        if self.d == 'N':
            if self.y > cow.y or cow.x > self.x:
                return True
            return False
        else:
            if self.x > cow.x or cow.y > self.y:
                return True
            return False 
        
n = int(input().strip())
cows = []

for i in range(n):
    line = input().strip().split()
    cows.append(Cow(line[1], line[2], line[0]))

while True:
    eatenThisHour = set()
    for cow in cows:
        cow.maybeStop()
        if cow.eat():
            eatenThisHour.add(cow.cord())
        cow.move()
    eatenCells = eatenCells.union(eatenThisHour)
    for cow in cows:
        cow.maybeStop()
    for cow in cows:
        if not cow.alive:
            continue
        infinite = True
        for cow2 in cows:
            if not cow.outOfWay(cow2):
                infinite = False
                break
        if infinite:
            cow.eaten = 'Infinity'
            cow.alive = False
    
    allDead = True
    for cow in cows:
        if cow.alive:
            allDead = False
            break
    if allDead:
        break

for cow in cows:
    print(cow.eaten)
    

