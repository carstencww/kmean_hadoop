#!/bin/bash
NumOfP=5

n="${NumOfP}part"
for j in `seq 0 1 $NumOfP`; do
i="-$j"
out="$j-${NumOfP}_centroid_result.txt"
rm ./data/image_train.txt
rm ./data/image_test.txt
rm ./data/label_test.txt
rm ./data/label_train.txt

ls ./data/$n | grep 'image' | grep -v -e "$i" | while read filename
do
cat ./data/$n/$filename >> ./data/image_train.txt
done

ls ./data/$n | grep 'image' | grep -e "$i" | while read filename
do
cp ./data/$n/$filename ./data/image_test.txt
done

hadoop dfs -copyFromLocal -f ./data/image_train.txt input/
python ./random_init.py
./kmean_run.sh

cp ./centroid_result.txt ./$out

done




































