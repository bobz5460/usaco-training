import sys
sys.stdin = open("traffic.in", "r")
sys.stdout = open("traffic.out", "w")
ramps = []
sensorRanges = []
n = int(sys.stdin.readline().strip())
for i in range(n):
    ramp, lower, upper = sys.stdin.readline().strip().split()
    lower, upper = int(lower), int(upper)
    if ramp == 'none':
        sensorRanges.append((lower, upper))
        ramps.append((None,None))
    elif ramp == 'on':
        ramps.append((lower, upper))
        sensorRanges.append((None,None))
    else:
        ramps.append((-lower, -upper))
        sensorRanges.append((None,None))
first = True
in_a_row = True
straightEnd = []
for i in range(n):
    if first and sensorRanges[i] == (None, None):
        continue
    if sensorRanges[i] == (None, None):
        in_a_row = False
    first = False
    if in_a_row:
        straightEnd.append(sensorRanges[i])
        continue
    in_a_row = True
    maxMin, minMax = 0, 0
    for e in range(0,len(straightEnd)):
        if straightEnd[e][0] > maxMin or maxMin == 0:
            maxMin = straightEnd[e][0]
        if straightEnd[e][1] < minMax or minMax == 0:
            minMax = straightEnd[e][1]
    rampMin, rampMax = ramps[i][0], ramps[i][1]
    
    maxMin += ramps[i][1]
    minMax += ramps[i][0]
    straightEnd = [(maxMin, minMax)]

first = True
in_a_row = True
straightStart = []
for i in range(n-1, -1, -1):
    if first and sensorRanges[i] == (None, None):
        continue
    if sensorRanges[i] == (None, None):
        in_a_row = False
    first = False
    if in_a_row:
        straightStart.append(sensorRanges[i])
        continue
    in_a_row = True
    maxMin, minMax = 0, 0
    for e in range(0,len(straightStart)):
        if straightStart[e][0] > maxMin or maxMin == 0:
            maxMin = straightStart[e][0]
        if straightStart[e][1] < minMax or minMax == 0:
            minMax = straightStart[e][1]
    rampMin, rampMax = ramps[i][0], ramps[i][1]
    maxMin -= ramps[i][1]
    minMax -= ramps[i][0]
    straightStart = [(maxMin, minMax)]

print(straightStart[0][0], straightStart[0][1])
print(straightEnd[0][0], straightEnd[0][1])