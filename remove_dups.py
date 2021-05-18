# removes all duplicates from a input text file
# then writes each element to their own line
# file is kept under the same name but there
# is a temp file used in between
# command line arg 1: input file

import sys 
import os

# set to store elements seen
s = set()

# create a temp file to store file without
# duplicates and element separated by \n
# NOTE: MAKE SURE YOU DON'T HAVE A FILE NAMED 'temp00000.txt'
toWrite = open('temp00000.txt', 'w')

# read through file and write new elements
# to new file
with open(sys.argv[1], 'rt') as file:
    for line in file:
        for element in line.split():
            if element not in s:
                toWrite.write(element + "\n")
                s.add(element)

# close file
toWrite.close()

# rename new file to be name of old file
os.remove(sys.argv[1])
os.rename(r'temp00000.txt', sys.argv[1])