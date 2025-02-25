#a and b are INTEGERS
import sys
t = int(input().strip())
tests = []
answers = [0,0]
for i in range(t):
    tests.append(int(input().strip()))
def round(a, b):
    x = int(str(a)[-b])
    temp = ''
    if x >= 5:
        a+=pow(10, b)
    for i in range(-b, 0):
        temp += str(a)[i]
    return a-int(temp)

def chainround(a, b):
    for i in range(1, b+1):
        a = round(a, i)
    return a
number = 0
for j in range(2, max(tests)+1):
    p = len(str(j)) - 1
    if pow(10, p) < j:
        p+=1
    if round(j, p) != chainround(j, p):
        number+=1
    answers.append(number)
for i in tests:
    print(answers[i])

