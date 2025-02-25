"""
ID: bzhang51
LANG: PYTHON3
TASK: test
"""
fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')
numbeads = int(fin.readline())
bead = fin.readline()
beads = bead+bead
maximum = None
for i in range(numbeads):
    counter = 1
    first = beads[i]
    while True:
        if beads[i+counter] == first:
            counter+=1
            continue
        else:
            if maximum is None or maximum < counter:
                maximum = counter
            break
        
print(counter)
#fout.write()
#fout.close()