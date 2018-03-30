#!/usr/bin/env python
import sys
import numpy as np
cnt = 0
origin_centroid = [0]*10

class_cnt = [0]*10

with open("./train_centroid.txt","r") as cens:
	for cen in cens:
		cen = cen.strip()
		class_no , centroid = cen.split('\t')
		class_no = int(class_no)
		centroid = centroid.split(",")
		origin_centroid[class_no] = [float(x) for x in centroid]
origin_centroid = np.asarray(origin_centroid)
class_sum = np.zeros((10,origin_centroid.shape[1]))

for line in sys.stdin:
	cnt+=1
	line = line.strip()
	pixels = line.split(",")
	pixels = [float(x) for x in pixels]
	pixels = np.asarray(pixels)
	class_idx = np.linalg.norm(origin_centroid - pixels,axis=1).argmin()
	class_cnt[class_idx]+=1
	class_sum[class_idx]+=pixels
for i in range(0,10):
	class_sum[i] = class_sum[i] / float(class_cnt[i])
	print(str(i)+"\t"+str(class_cnt[i])+":"+",".join(str(x) for x in class_sum[i]))
