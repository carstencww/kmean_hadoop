import numpy as np
import os
import struct

#train-images-idx3-ubyte,t10k-images-idx3-ubyte,train-labels-idx1-ubyte,t10k-labels-idx1-ubyte
labelfile = "train-labels-idx1-ubyte" , "t10k-labels-idx1-ubyte"
imagefile = "train-images-idx3-ubyte" , "t10k-images-idx3-ubyte"
txtlabel = "label_train.txt" , "label_test.txt"
txtimage = "image_train.txt" , "image_test.txt"

for i in range(0,2):
	with open(labelfile[i], 'rb') as idxlb:
		MagicN, Num = struct.unpack(">II", idxlb.read(8))
		labels = np.fromfile(idxlb, dtype=np.int8)
	print(MagicN)
	print(Num)
	with open(txtlabel[i],'w') as txtlbf:
		for label in labels:
			txtlbf.write(str(label)+'\n')

	with open(imagefile[i], 'rb') as idxim:
		magicn, num, rows, cols = struct.unpack(">IIII", idxim.read(16))
		images = np.fromfile(idxim, dtype=np.uint8).reshape(len(labels), rows * cols)
	print(magicn)
	print(num)
	print(rows)
#print(images)
	with open(txtimage[i],'w') as txtima:
		for image in images:
			imagetxt = ",".join(str(x) for x in image)
			txtima.write(imagetxt+'\n')

