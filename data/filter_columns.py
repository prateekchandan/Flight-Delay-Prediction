import pandas as pd
import numpy as np
import sys
import csv
from sklearn.feature_extraction import DictVectorizer as DV


if len(sys.argv) < 3:
    sys.exit("Usage: python filter_columns.py <inp filename> <out filename>")

filename = sys.argv[1]
outfilename = sys.argv[2]
df = pd.read_csv(filename, header=0)

cols = ['Year','Month','DayOfWeek','DepTime','CRSDepTime','ArrTime','CRSArrTime','UniqueCarrier','ActualElapsedTime','CRSElapsedTime','AirTime','ArrDelay','DepDelay','Origin','Dest','Distance','Cancelled','source  Dry Bulb Temp','source  Dew Point Temp','source  Wet Bulb Temp','source  % Relative Humidity','source  Wind Speed (kt)','source  Station Pressure','source  Sea Level Pressure','dest  Dry Bulb Temp','dest  Dew Point Temp','dest  Wet Bulb Temp','dest  % Relative Humidity','dest  Wind Speed (kt)','dest  Station Pressure','dest  Sea Level Pressure']
#print cols

df = df[cols]
#df.info()

neg_list = ['UniqueCarrier', 'Origin', 'Dest', 'source  Visibility', 'dest  Visibility']

numeric_cols = [item for item in cols if item not in neg_list]


#df['source  Wet Bulb Temp'] = df['source  Wet Bulb Temp'].replace('-', '')


df.to_csv('filtered.csv', sep=',', index= False)

inter = open('filtered.csv', 'rb')
final = open('final.csv', 'wb')

final_writer = csv.writer(final)

num_list = [l for l in range(0,31)]
neg_list = [7,13,14]

months = [i for i in range(1,13)]
days = [i for i in range(1,8)]

final_num_list = [item for item in num_list if item not in neg_list]
first = True

first_line = ',1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7'

carrier = ['WN', 'DL', 'AA', 'UA', 'US', 'NW', 'CO', 'MQ', 'HP', 'OO', 'TW', 'AS', 'XE', 'EV', 'OH', 'FL', 'DH', 'B6', 'YV', 'TZ']
origin = ['ORD', 'ATL', 'DFW', 'LAX', 'PHX', 'IAH', 'DEN', 'DTW', 'MSP', 'LAS', 'STL', 'EWR', 'SFO', 'CLT', 'BOS', 'PHL', 'LGA', 'CVG', 'MCO', 'SEA']
dest = ['ORD', 'ATL', 'DFW', 'LAX', 'PHX', 'IAH', 'DEN', 'DTW', 'MSP', 'LAS', 'STL', 'EWR', 'SFO', 'CLT', 'BOS', 'PHL', 'LGA', 'CVG', 'MCO', 'SEA']

carrier_dict = {}
origin_dict = {}
dest_dict = {}


for i in range(0,20):
    carrier_dict[carrier[i]] = i
    origin_dict[origin[i]] = i
    dest_dict[dest[i]] = i


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

for line in inter:
    dummy_row = ['0' for i in range(0,79)]
    
    if first:
        first = False
        
        final.write(line.strip()+first_line+','+','.join(carrier)+','+','.join(origin)+','+','.join(dest)+'\n')
        continue
    l = line.strip().split(',')

    m = int(l[1])
    d = int(l[2])

    dummy_row[m-1] = '1'
    dummy_row[11+d] = '1'

    car = l[7]
    org = l[13]
    dst = l[14]

    if car in carrier_dict:
        dummy_row[19+carrier_dict[car]] = '1'
    if org in origin_dict:
        dummy_row[39+origin_dict[org]] = '1'
    if dst in dest_dict:
        dummy_row[59+dest_dict[dst]] = '1'
    
    l = l + dummy_row
    #print len(l)
    for j in final_num_list:
        #print j
        if not(is_number(str(l[j]))):
            l[j] = '-'
    final_writer.writerow(l)
final.close()


df = pd.read_csv('final.csv', header=0)
df.info()

for col in numeric_cols:
    
    df[col] = df[col].replace('-', np.nan)
    df[col] = df[col].astype(float)
    df[col] = df[col].interpolate()

df = df.drop(['Month', 'DayOfWeek', 'Origin', 'Dest', 'UniqueCarrier'], axis=1)
df.info()
df.to_csv(outfilename, index=False)


