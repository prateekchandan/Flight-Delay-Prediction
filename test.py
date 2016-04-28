import pandas as pd
import numpy as np
import csv
import sys
from sklearn import linear_model, svm, ensemble
import cPickle

from sklearn import tree
from sklearn import cross_validation

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
    message = bcolors.BOLD + "Usage: python test.py <input file>" + bcolors.ENDC
    sys.exit(message)

filename = sys.argv[1]
inp = open(filename, 'rb')

with open('linear_regression.pkl', 'rb') as fid:
    clf = cPickle.load(fid)

outfile = open('test_output.csv', 'wb')

ind = 0
for line in inp:
    inp_array = line.strip().split(',')
    inp_array = [float(i) for i in inp_array]
    y = clf.predict(inp_array)
    outfile.write(str(ind)+', '+str(int(y[0]))+'\n')
    ind += 1

outfile.close()
