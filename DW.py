#!/usr/bin/env python3

import random
import os

i = 1
datei = "DW.txt"
worterbuch = dict()
stream = open(datei, "r")
for line in stream:
    paar = line.split("\t")
    if len(paar)>1 and paar[2]:
        worterbuch[i] = (paar[0], paar[2].strip())
        i += 1
stream.close()
while True:
    num = random.randint(1, len(worterbuch))
    print("***Was ist die Definition von {}?***".format(worterbuch[num][0]))
    x = input()
    if x == "x":
        os.system("clear")
        print("Drücke X um die Lösung zu erhalten\n")
        print("Die richtige Antwort für '{}' wäre: {}\n\n\n".format(worterbuch[num][0], worterbuch[num][1]))
    else:
        break
    






