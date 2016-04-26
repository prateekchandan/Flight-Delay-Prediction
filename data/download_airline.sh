#!/bin/bash

mkdir -p airline_data
cd airline_data
for i in `seq 1997 2006`
do
	filename=$i".csv"
	if [ ! -f $filename ];then
		wget "http://stat-computing.org/dataexpo/2009/"$i".csv.bz2" &
	fi
done

wait

for i in `seq 1997 2006`
do
        filename=$i".csv"
        if [ ! -f $filename ];then
                bzip2 -d $i".csv.bz2" &
        fi
done

wait
