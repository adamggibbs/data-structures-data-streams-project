# Takes every int up to a specified max 
# int and writes each int to one 
# of two files based on a specified bias
# command line arg 1: max int
# command line arg 2: output file 1 (get int with p=bias)
# command line arg 3: output file 2 (get int with p=1-bias)
# command line arg 4: bias value

import sys 
import random

f1_bias = sys.argv[4]

# create output files
# NOTE: THIS OVERWRITES FILES WITH SAME NAME
f1 = open(sys.argv[2], "w")
f2 = open(sys.argv[3], "w")

# loop from 0 to max int and write each
# int to either file 1 or file 2
for i in range(0, int(sys.argv[1])):
    if random.random() < f1_bias:
        f1.write(str(i) + "\n")
    else:
        f2.write(str(i) + "\n")

# close files
f1.close()
f2.close()