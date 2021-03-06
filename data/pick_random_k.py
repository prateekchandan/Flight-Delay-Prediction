#!/usr/bin/env python
#
# This python file creates a random input data by random sampling from a list of multiple files
# Author - Prateek & Nishant
#
# Input year from command line
# Usage : Usage: python pick_random_k.py <k=number of rows required> <csvfile1> <csvfile2>...

import sys
import csv
import random
import numpy as np

class bcolors:
    '''
    Class bcolor used for printing pretty messages
    '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Check for arg correctoness
if len(sys.argv) < 2:
    message = bcolors.BOLD + "Usage: python pick_random_k.py <k=number of rows required> <csvfile1> <csvfile2>..." + bcolors.ENDC
    sys.exit(message)

# check if input is integer
try:
    reqd = int(sys.argv[1])
except:
    message = bcolors.FAIL + "expects integer second argument" + bcolors.ENDC
    sys.exit(message)

# returns a progress string denoted by progress
def progress_string(reps):
    s = ""
    for i in range(0, reps):
        s += '='
    return bcolors.OKGREEN + s + bcolors.ENDC

# Initialize the toolbar
def toolbar_init(message):
    # setup toolbar
    message = bcolors.OKBLUE + message + bcolors.ENDC
    sys.stdout.write("%s: [%s]" % (message, " " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

# Makes the progress bar
def make_progress(toolbar_accum, prev_toolbar_accum):
    sys.stdout.write("\b" * (prev_toolbar_accum)) # return to start of line, after '['
    sys.stdout.write(progress_string(int(toolbar_accum)))
    sys.stdout.flush()


# output file
outputfile = open('randomoutput_'+str(reqd)+'.csv', 'wb')

# lines to be taken from each file
lines_file = int(reqd/(len(sys.argv)-2))
print "lines per file: " + str(lines_file)
done = False

toolbar_width = 30

#loop over all input files
for i in range(2, len(sys.argv)):
    print i
    # check if file is correct
    try:
        csvfile = open(sys.argv[i], 'rb')
    except:
        message = bcolors.FAIL + "csv data file " + csvfile + " does not exist" + bcolors.ENDC
        sys.exit(message)

    num_lines = 0
    first_line = ""
    first = True

    # Count the number of lines in the file
    toolbar_init("Finding number of lines")
    toolbar_accum = 0
    prev_toolbar_accum = 0
    for line in csvfile:
        toolbar_accum += toolbar_width*1.0/6500000
        make_progress(toolbar_accum, prev_toolbar_accum)
        prev_toolbar_accum = int(toolbar_accum)
        #ignore first line
        if first:
            first_line = line
            first = False
        num_lines += 1
    make_progress(toolbar_width, prev_toolbar_accum)
    prev_toolbar_accum = 0
    sys.stdout.write("\n")
    csvfile.close()
    
    
    if not(done):
        done = True
        outputfile.write(first_line)

    try:
        csvfile = open(sys.argv[i], 'rb')
    except:
        message = bcolors.FAIL + "csv data file " + csvfile + " does not exist" + bcolors.ENDC
        sys.exit(message)

    # The probabbility 'p' with which each line can be selected
    p = lines_file*1.0/num_lines
    num_written = 0
    toolbar_init("Picking random lines")
    toolbar_accum = 0
    prev_toolbar_accum = 0
    # loop over each lines
    for line in csvfile:
        #print line
        toolbar_accum += toolbar_width*1.0/num_lines
        make_progress(toolbar_accum, prev_toolbar_accum)
        prev_toolbar_accum = int(toolbar_accum)
        # genarate a uniform random sample
        rand = np.random.uniform()
        # if correclty sampled , take in input data
        if rand <= p:
            outputfile.write(line)
            num_written += 1
    #print progress
    make_progress(toolbar_width, prev_toolbar_accum)
    prev_toolbar_accum = 0
    sys.stdout.write("\n")
    print "Number of lines written: " + str(num_written)

    csvfile.close()

outputfile.close()
    
    
