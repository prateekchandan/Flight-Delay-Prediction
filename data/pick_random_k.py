import sys
import csv
import random
import numpy as np

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) < 2:
    message = bcolors.BOLD + "Usage: python pick_random_k.py <k=number of rows required> <csvfile1> <csvfile2>..." + bcolors.ENDC
    sys.exit(message)

try:
    reqd = int(sys.argv[1])
except:
    message = bcolors.FAIL + "expects integer second argument" + bcolors.ENDC
    sys.exit(message)

outputfile = open('randomoutput.csv', 'wb')
    
lines_file = int(reqd/(len(sys.argv)-2))
print "lines per file: " + str(lines_file)
done = False

for i in range(2, len(sys.argv)):
    print i
    try:
        csvfile = open(sys.argv[i], 'rb')
    except:
        message = bcolors.FAIL + "csv data file " + csvfile + " does not exist" + bcolors.ENDC
        sys.exit(message)

    num_lines = 0
    first_line = ""
    first = True
    for line in csvfile:
        if first:
            first_line = line
            first = False
        num_lines += 1
    csvfile.close()
    
    #random_list = random.sample(range(1, num_lines), lines_file)
    #print random_list
    if not(done):
        done = True
        outputfile.write(first_line)

    try:
        csvfile = open(sys.argv[i], 'rb')
    except:
        message = bcolors.FAIL + "csv data file " + csvfile + " does not exist" + bcolors.ENDC
        sys.exit(message)

    p = lines_file*1.0/num_lines
    num_written = 0
    print "picking random lines"
    for line in csvfile:
        #print line
        
        rand = np.random.uniform()
        if rand <= p:
            outputfile.write(line)
            num_written += 1
    print "Number of lines written: " + str(num_written)

    csvfile.close()

outputfile.close()
    
    
