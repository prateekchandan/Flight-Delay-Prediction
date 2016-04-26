#!/bin/bash
mkdir -p weather

#downloading data

for i in `seq 1997 2006`
do
	for j in `seq 1 12`
	do
		if [ $j -lt 10 ] ; then
			filename=$i"0$j.tar.gz"
		else
			filename="$i$j.tar.gz"
		fi
		path="./weather/"$filename
		if [ ! -f $path ];then
			url="http://www.ncdc.noaa.gov/orders/qclcd/"$filename
			#echo $url $path
			wget -O $path $url &
		fi
	done
	wait
done

cd weather

#extracting data
for i in `seq 1997 2006`
do
	for j in `seq 1 12`
	do
		if [ $j -lt 10 ] ; then
			filename=$i"0$j"
		else
			filename="$i$j"
		fi
		path=$filename"/"$filename"daily.txt"
		zipname=$filename".tar.gz"
		if [ ! -f $path ];then
			if [ -f $zipname ];then
				mkdir -p $filename
				tar -xvzf $zipname -C $filename &
			fi;
		fi
	done
	wait
done
