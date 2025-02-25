import sys
thing = {}
sys.stdin = open("teleport.in", "r")
sys.stdout = open("teleport.out", "w")
inp = sys.stdin.readline()
a, b, x, y = inp.split(" ")
a, b, x, y, = int(a), int(b), int(x), int(y)
distance = 0
distance2 = 0
disax = abs(a-x)
disay = abs(a-y)
if disax<disay:
    distance+=disax
    distance+=abs(y-b)
else:
    distance+=disay
    distance+=abs(x-b)
disbx = abs(b-x)
disby = abs(b-y)
if disbx<disby:
    distance2+=disbx
    distance2+=abs(y-a)
else:
    distance2+=disay
    distance2+=abs(x-a)
distanceab = abs(a-b)
print(min(distance, distance2, distanceab))

