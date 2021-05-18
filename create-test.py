
import sys 
import random

f1 = open(sys.argv[2], "w")
f2 = open(sys.argv[3], "w")

for i in range(0,int(sys.argv[1])):
    if random.random() < 0.5:
        f1.write(str(i) + "\n")
    else:
        f2.write(str(i) + "\n")

f1.close()
f2.close()