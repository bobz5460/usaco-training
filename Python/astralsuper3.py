import sys

T = int(input().strip())


def test():
    N, A, B = input().strip().split()
    N, A, B = int(N), int(A), int(B)
    states = [[0]*N for i in range(N)]
    array = []
    for i in range(N):
        row = input().strip()
        array.append(row)
        for j in range(N):
            if row[j] == 'B':
                states[i][j] = 1
                i0 = i - B
                j0 = j - A
                if i0 < 0 or j0 < 0:
                    return -1
                states[i0][j0] = 1
    for i in range(N):
        for j in range(N):
            if array[i][j] == 'W':
                if states[i][j] == 1:
                    return -1
            elif array[i][j] == 'G':
                i0 = i - B
                j0 = j - A
                if i0 < 0 or j0 < 0 or states[i0][j0] == 0:
                    states[i][j] = 1
    count = 0
    for i in range(N):
        count += sum(states[i])
    return count


for n in range(T):
    print(test())
                  

