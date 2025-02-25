n = int(input("Input number: "))
mylist = []
while True:
    if n == 1:
        mylist.append(1)
        break
    elif n%2 == 0:
        n /= 2
        mylist.append(n)
    else:
        n = n*3
        n += 1
        mylist.append(n)
print(mylist)

