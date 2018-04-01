#!/usr/bin/env python
import numpy as np

result_centroid = [0]*10

with open("./centroid_result.txt","r") as cens:
	for cen in cens:
		cen = cen.strip()
		class_no , centroid = cen.split('\t')
		class_no = int(class_no)
		centroid = centroid.split(",")
		result_centroid[class_no] = [float(x) for x in centroid]
result_centroid = np.asarray(result_centroid)

true_label = []

class_no = []
dist = [{} for i in range(10)]
with open("../data/image_train.txt","r") as images:
	idx = 0
	for image in images:
		image = image.strip()
		image = image.split(",")
		image = [float(x) for x in image]
		image = np.asarray(image)
		error = np.linalg.norm(result_centroid - image, axis=1)
		result = error.argmin()
		class_no.append(result)
		dist[result][idx] = error[result]
		idx += 1
for i in range(10):
	elements=sorted(dist[i].items(), key=itemgetter(1),reverse=False)


#print(class_cnt)
