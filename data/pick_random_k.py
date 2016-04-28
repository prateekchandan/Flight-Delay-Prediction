import sys
import csv
import random

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

    csvfile_lines = csvfile.readlines()
    random_choice = random.sample(csvfile_lines[1:], lines_file)
    csvfile.close()

    if not(done):
        done = True
        outputfile.write(csvfile_lines[0])
        
    outputfile.write("".join(random_choice))
    
    
