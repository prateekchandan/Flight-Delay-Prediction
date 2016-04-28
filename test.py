import pandas as pd
import numpy as np
import csv
import sys
from sklearn import linear_model, svm, ensemble
import cPickle

from sklearn import tree
from sklearn import cross_validation

if len(sys.argv) < 2:
    print "Usage: python test.py <input file>"

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
