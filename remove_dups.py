import sys 

s = set()

toWrite = open(sys.argv[2], 'w')

with open(sys.argv[1], 'rt') as file:
    for line in file:
        for element in line.split():
            if element not in s:
                toWrite.write(element + "\n")
                s.add(element)

toWrite.close()