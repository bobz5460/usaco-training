import sys
sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")
speedLimits = []
speedsDriven = []
roadSegments = []
drivenSegments = []
numRoadSegments, numDrivenSegments = sys.stdin.readline().strip().split()
numRoadSegments, numDrivenSegments = int(numRoadSegments), int(numDrivenSegments)
for i in range(numRoadSegments):
    roadSegments.append(sys.stdin.readline().strip().split())
for i in range(numDrivenSegments):
    drivenSegments.append(sys.stdin.readline().strip().split())
for i in range(numRoadSegments):
    currentLimit = roadSegments[i][1]
    numMiles = int(roadSegments[i][0])
    for i in range(numMiles):
        speedLimits.append(int(currentLimit))
for i in range(numDrivenSegments):
    currentSpeed = drivenSegments[i][1]
    numMiles = int(drivenSegments[i][0])
    for i in range(numMiles):
        speedsDriven.append(int(currentSpeed))
maxOver = 0
for i in range(100):
    maxOver = max(maxOver, speedsDriven[i]-speedLimits[i])

print(maxOver)