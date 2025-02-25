import sys
T = int(input().strip())
N, A, B = input().strip().split()
N, A, B = int(N), int(A), int(B)
array = []
states = [[-1]*N]*N
for i in range(N):
    array.append(input().strip())
def main(array, A, B):
    count = 0
    states = [[-1]*N for i in range(N)]
    for x in range(N):
        for y in range(N):
            if array[x][y] == 'W':
                states[x][y] = 0
    for x in range(N):
        for y in range(N):
            if array[x][y] == 'B':
                if x-B < 0 or y-A < 0:
                    return -1
                if states[x-B][y-A] == -1:
                    states[x-B][y-A] = 1
                elif states[x-B][y-A] == 0:
                    return -1
    for x in range(N):
        for y in range(N):
            if array[x][y] == 'G':
                if x-B < 0 or y-A < 0:
                    return -1
                if states[x-B][y-A] == 0:
                    if states[x][y] == -1:
                        states[x][y] = 1
                    elif states[x][y] == 0:
                        return -1
                if states[x-B][y-A] == 1:
                    if states[x][y] == -1:
                        states[x][y] = 0
    for x in range(N):
        for y in range(N):
            if states[x][y] == 1:
                count +=1
    return count
print(main(array, A, B))
                        

