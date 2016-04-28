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
    message = bcolors.BOLD + "Usage: python  train.py <train_data>" + bcolors.ENDC
    sys.exit(message)

try:
    df = pd.read_csv(sys.argv[1],header=0)
except:
    message = bcolors.FAIL + " file " + sys.argv[1] + " does not exist" + bcolors.ENDC
    sys.exit(message)


y1 = df['DepDelay'].values
y2 = df['ArrDelay'].values

df = df.drop(['DepDelay','ArrDelay'], axis=1)
X = df.values

#X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y1,test_size=0.3,random_state=0)

clf = linear_model.LinearRegression()
#scores = cross_validation.cross_val_score(clf, X, y1, scoring = 'mean_squared_error', cv=5)
clf.fit(X,y1)
#print "Linear regression: " + str(scores)

with open('linear_regression.pkl', 'wb') as fid:
    cPickle.dump(clf, fid)

"""

clf = linear_model.Ridge (alpha = .5)
scores = cross_validation.cross_val_score(clf, X, y1, scoring = 'mean_squared_error', cv=5)
print "Ridge regression: " + str(scores)


params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 1,
          'learning_rate': 0.01, 'loss': 'ls'}
clf = ensemble.GradientBoostingRegressor(**params)
scores = cross_validation.cross_val_score(clf, X, y1, scoring = 'mean_squared_error', cv=5)
print "gradient boosting: " + str(scores)
"""
