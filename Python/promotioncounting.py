#Too Lazy
import sys
sys.stdin = open("promote.in", "r")
sys.stdout = open("promote.out", "w")
bronze = sys.stdin.readline()
silver = sys.stdin.readline()
gold = sys.stdin.readline()
platinum = sys.stdin.readline()
bstart, bend = bronze.split(" ")
sstart, send = silver.split(" ")
gstart, gend = gold.split(" ")
pstart, pend = platinum.split(" ")
bstart, sstart, gstart, pstart, bend, send, gend, pend = int(bstart), int(sstart), int(gstart), int(pstart), int(bend), int(send), int(gend), int(pend)
startTotal = bstart+sstart+gstart+pstart
endTotal = bend+send+gend+pend
newcontestents = endTotal-startTotal
bstart += newcontestents
promotions = {'silver': 0, 'gold': 0, 'platinum': 0}

