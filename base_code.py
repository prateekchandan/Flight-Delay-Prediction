import pandas as pd
import numpy as np
from sklearn import linear_model, svm
from sklearn import cross_validation


df = pd.read_csv('2008_new.csv',header=0)
print("----------------------------------------------------------------------------------")
#df.info()
df = df[df.Cancelled == 0]
df = df[df.Diverted == 0]
cols = ['DayOfWeek', 'UniqueCarrier', 'Origin', 'Dest', 'Distance', 'ArrDelay', 'DepDelay']
df = df[cols]

df.info()



dummies = []
cols = ['DayOfWeek','UniqueCarrier','Origin','Dest']

for col in cols:
	dummies.append(pd.get_dummies(df[col]))

data_dummies = pd.concat(dummies, axis=1)
 
df = pd.concat((df,data_dummies),axis=1)


df = df.drop(cols,axis=1)
print("----------------------------------------------------------------------------------")
df.info()


y1 = df['ArrDelay'].values
y2 = df['DepDelay'].values

df.drop(['ArrDelay','DepDelay'],axis=1)
X = df.values

clf = linear_model.LinearRegression()
clf.fit(X, y1)

X_test = df.values
y_res = clf.predict(X_test)
y_res = np.around(y_res)
np.savetxt('outArrDelay.csv', y_res, fmt="%d")

