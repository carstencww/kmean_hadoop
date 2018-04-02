import numpy as np
from random import sample
#np.random.seed(0)
imagefile = "./data/image_train.txt"
centroid_f = "train_centroid.txt"
images= []

with open(imagefile, "r") as f:
    for line in f:
        line = line.strip()
        line = line.split(",")
        line = [int(x) for x in line]
        images.append(line)
images = np.asarray(images)

cans = sample(xrange(0,len(images)),10)
candidates = [images[can] for can in cans]

#print(np.linalg.norm(images - candidates[0],axis=1))
print(cans)
with open(centroid_f, "w") as cenf:
    i=0
    for candidate in candidates:
        cenf.write(str(i)+'\t'+",".join(str(x) for x in candidate)+'\n')
        i+=1
