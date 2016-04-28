import pandas as pd
import numpy as np
import csv
import sys
from sklearn import linear_model, svm

from sklearn import tree
from sklearn import cross_validation


df = pd.read_csv('./data/final_100000.csv',header=0)


y1 = df['DepDelay'].values
y2 = df['ArrDelay'].values

df = df.drop(['DepDelay','ArrDelay'], axis=1)
X = df.values

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y1,test_size=0.3,random_state=0)

clf = linear_model.LinearRegression()

clf.fit(X_train,y_train)
scores = cross_validation.cross_val_score(clf, X, y1, scoring = 'mean_squared_error', cv=5)

print scores
