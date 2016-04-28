#!/usr/bin/env python
#
# This python file plots multiple histogram for inputs
# Author - Prateek & Nishant
#


import matplotlib.pyplot as plt
import random
import sys
import csv

# Save histogram of x and y to file
def histPlotSave(x,y,filename):
	plt.bar(y,x)
	plt.savefig(filename)


# Class bcolors
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
    message = bcolors.BOLD + "Usage: python  histplot.py <filtered_data>" + bcolors.ENDC
    sys.exit(message)

try:
    inpFile = open(sys.argv[1],'rb')
except:
    message = bcolors.FAIL + "csv data file " + argv[1] + " does not exist" + bcolors.ENDC
    sys.exit(message)

header = []
maxArr = []
minArr = []
inpLen = 0

#loop over input file
for line in inpFile:
	line = line.split(",")
	#read header
	if len(header) == 0:
		header = line
		inpLen = len(line)
		continue

	#find max and min by allocatin second row
	if len(maxArr)==0:
		maxArr=line
		minArr=line

	for x in range(0,inpLen):
		if maxArr[x] < line[x]:
			maxArr[x] = line[x]
		if minArr[x] > line[x]
			minArr = line[x]
inpFile.close()
#We have the header and max min now

inpFile = open(sys.argv[1],'rb')
binArrays = inpLen*{}

#Find bins values now

# pass over header
if line in inpFile:
	pass

# find bins
count=0
for line in inpFile:
	count+=1
	for x in range(0,inpLen-2):
		



