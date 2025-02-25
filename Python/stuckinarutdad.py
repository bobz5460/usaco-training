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
            self.maybeStop()
    
    def eat(self):
        self.maybeStop()
        if self.alive:
            self.eaten += 1
            return True
        return False
    
    def outOfWay(self, cow):
        if self.d == cow.d:
            return True   
        if self.d == 'N' and self.y > cow.y:
            return True
        elif self.d == 'E' and self.x > cow.x:
            return True
        return False
        
n = int(input().strip())
cows = []

for i in range(n):
    line = input().strip().split()
    cows.append(Cow(line[1], line[2], line[0]))
live_cows = cows.copy()

while live_cows:
    eatenThisHour = set()
    for cow in live_cows.copy():
        if cow.eat():
            eatenThisHour.add(cow.cord())
        cow.move()
        if not cow.alive:
            live_cows.remove(cow)
    eatenCells = eatenCells.union(eatenThisHour)

    for cow in live_cows.copy():
        infinite = True
        for cow2 in cows:
            if not cow.outOfWay(cow2):
                infinite = False
                break
        if infinite:
            cow.eaten = 'Infinity'
            cow.alive = False
            live_cows.remove(cow) 
for cow in cows:
    print(cow.eaten)
    

