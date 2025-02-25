thing = input("Enter maths: ")
thing = thing.replace(' ', '')

def add(num1, num2, op):
    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2
    else:
        return num1/num2
while True:
    if len(thing) == 1:
        break
    num1 = thing[0]
    op = thing[1]
    num2 = thing[2]
    otherthing = add(int(num1), int(num2), op)
    thing = thing[3:]
    thing = str(otherthing)+thing
print(thing)