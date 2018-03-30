#!/usr/bin/env python
import sys
import numpy as np
cnt = 0
origin_centroid
class_sum
class_cnt = 
for line in sys.stdin:
	cnt+=1
	line = line.strip()
	pixels = line.split(",")

	for word in words:
		if wc.has_key(word):
			wc[word]= wc[word] + 1
		else:
			wc[word] = 1

thr=int(cnt*0.005)
#print("threshold",thr)
fw=[]
for key,value in wc.iteritems():
	if value>=thr:
		fw.append(key)
fw.sort()
wc={}
for i in range(len(fw)-1):
	for j in range(i+1, len(fw)):
		pair=(fw[i],fw[j])
		wc[pair]=0

for words in context:
	for i in range(len(words)-1):
		for j in range(i+1,len(words)):
			pair=(words[i],words[j])
			try:
				wc[pair]=wc[pair]+1
			except:
				pass

for key,value in wc.iteritems():
	if value>thr:
		print(str(key)+'\t'+str(value))
print("__NumB"+'\t'+str(cnt))
