# Takes a text file and splits each element
# amongst two files based on a specified bias
# command line arg 1: input file
# command line arg 2: output file 1 (get element with p=bias)
# command line arg 3: output file 2 (get element with p=1-bias)
# command line arg 4: bias value
 
import sys 
import random

# probability element gets written to file 1
f1_bias = float(sys.argv[4])

# create output files
# NOTE: THIS OVERWRITES FILES WITH SAME NAME
f1 = open(sys.argv[2], "w")
f2 = open(sys.argv[3], "w")

# read in text file and write each element to
# either file 1 or file 2
with open(sys.argv[1], 'rt') as file:
    for line in file:
        for element in line.split():
            if random.random() < f1_bias:
                f1.write(line)
            else:
                f2.write(line)

# close files
f1.close()
f2.close()