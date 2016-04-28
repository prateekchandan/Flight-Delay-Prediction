#!/bin/bash

# This script downloads and then unzips the airline data and stores it in the airline folder
# Author Prateek & Nishant

# create new folder
mkdir -p airline_data

cd airline_data

# Download all data
for i in `seq 1997 2006`
do
	filename=$i".csv"
	#ignore if csv already present
	if [ ! -f $filename ];then
		wget "http://stat-computing.org/dataexpo/2009/"$i".csv.bz2" &
	fi
done
wait

# Unzip them
for i in `seq 1997 2006`
do
        filename=$i".csv"
        if [ ! -f $filename ];then
                bzip2 -d $i".csv.bz2" &
        fi
done
wait
