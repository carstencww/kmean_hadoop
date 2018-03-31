#!/bin/bash

OUT_FILE=/user/ChanCarsten/hw1a
IN_FILE=/user/ChanCarsten/input/*
echo $PWD
hadoop dfs -rm -R $OUT_FILE
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-D mapred.map.tasks=100 \
-D mapred.reduce.tasks=10 \
-file $PWD/train_centroid.txt \
-file $PWD/part1a_map.py -mapper part1a_map.py \
-file $PWD/part1a_red.py -reducer part1a_red.py \
-input $IN_FILE \
-output $OUT_FILE

hadoop fs -getmerge $OUT_FILE ./centroid_result.txt
hadoop dfs -rm -R $OUT_FILE
