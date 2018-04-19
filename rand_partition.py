import numpy as np
n=5
filename=str(n)+"parts-"
foldername = "./data/"+"pca_"+str(n)+"part/"
#np.random.seed(0)
true_label = []
with open("./data/label_total.txt", "r") as f:
	for label in f:
		label = label.strip()
		label = int(label)
		true_label.append(label)

images= []

with open("./data/image_total.txt", "r") as f:
	for line in f:
		line = line.strip()
		line = line.split(",")
		line = [float(x) for x in line]
		images.append(line)
offset = np.random.randint(low=0,high=len(images))
for i in range(0,n):
	with open(foldername+"image_"+filename+str(i),"w") as f:
		for j in range(offset+i*len(images)/n, offset+(i+1)*len(images)/n):
			j = j % len(images)
			f.write(",".join(str(x) for x in images[j])+'\n')

for i in range(0,n):
        with open(foldername+"label_"+filename+str(i),"w") as f:
                for j in range(offset+i*len(images)/n, offset+(i+1)*len(images)/n):
			j = j % len(images)
			f.write(str(true_label[j])+'\n')



