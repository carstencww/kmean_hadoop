#/usr/bin/env python
import numpy as np
np.random.seed(0)
imagefile = "./data/label_train.txt"
cans = (2732, 35349, 33522, 22900, 16676, 21029, 32329, 26255, 13650, 56289)
labels= []

with open(imagefile, "r") as f:
    for line in f:
        line = line.strip()
        labels.append(line)

for can in cans:
    print(labels[can])
