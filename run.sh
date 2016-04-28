#!/bin/bash
# Main runner script for all files
# Author : Prateek & Nishant

#PREPARING DATA
echo "preparing data..."
sleep 1

cd data
./download_airline.sh
./download_weather.sh
wget http://stat-computing.org/dataexpo/2009/airports.csv
wget http://stat-computing.org/dataexpo/2009/carriers.csv

echo "All data downloaded.. Now merging data..."
sleep 1

#Merging files
python merge.py 1997
python merge.py 1998
python merge.py 1999
python merge.py 2000
python merge.py 2001
python merge.py 2002
python merge.py 2003
python merge.py 2004
python merge.py 2005
python merge.py 2006

echo "Fetiching some random data to do our task.."
sleep 1
#Random
python pick_random.py 10000 merged1997.csv merged1998.csv merged1999.csv merged2000.csv merged2001.csv merged2002.csv merged2003.csv merged2004.csv merged2005.csv merged2006.csv
python pick_random.py 100000 merged1997.csv merged1998.csv merged1999.csv merged2000.csv merged2001.csv merged2002.csv merged2003.csv merged2004.csv merged2005.csv merged2006.csv
python pick_random.py 1000000 merged1997.csv merged1998.csv merged1999.csv merged2000.csv merged2001.csv merged2002.csv merged2003.csv merged2004.csv merged2005.csv merged2006.csv

echo "randomdata generated.. cleaning other data now"
rm merged*
rm -rf airline_data
rm -rf weather

echo "Filtering data now.."
sleep 1
#Filtering
python filter_columns.py randomoutput_10000.csv filtered_10000.csv
python filter_columns.py randomoutput_100000.csv filtered_100000.csv
python filter_columns.py randomoutput_1000000.csv filtered_1000000.csv

#TRAINING AND TESTING MODEL NOW
cd ../

echo "Training data now"
python train.py ./data/filtered_1000000.py

