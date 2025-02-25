import sys
sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")
n = int(sys.stdin.readline().strip())
boards = []
freq = [0]*26
for i in range(n):
    boards.append((sys.stdin.readline().strip().split()))
for i in range(n):
    temp = [0]*26
    temp2 = [0]*26
    curWord = boards[i][0]
    for _ in curWord:
        temp[ord(_)-97] += 1
    curWord = boards[i][1]
    for _ in curWord:
        temp2[ord(_)-97] += 1
    for j in range(26):
        freq[j] += max(temp[j], temp2[j])
for t in freq:
    print(t)