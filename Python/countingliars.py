import sys
n = int(input().strip())
statement = []
number = []
minimum = 99999999999999999999999
for i in range(n):
    thing = input().strip().split()
    statement.append(thing[0])
    number.append(int(thing[1]))


for bessie in number:
    liars = 0
    for i in range(n):
        if statement[i] == 'G':
            if number[i] > bessie:
                liars += 1
        else:
            if number[i] < bessie:
                liars += 1
    minimum = min(liars, minimum)
print(minimum)