#/usr/bin/env python
import numpy as np
np.random.seed(0)
imagefile = "./data/label_train.txt"
#cans = (2732, 35349, 33522, 22900, 16676, 21029, 32329, 26255, 13650, 56289)
#cans = [12259, 36804, 48706, 33358, 33400, 49563, 14985, 30390, 39937, 6467]
#cans = [55682, 59872, 54762, 18615, 45685, 2639, 1779, 8364, 30247, 33249]
cans = [25842, 41358, 13650, 26838, 59452, 10417, 8104, 55513, 1448, 29048]
labels= []

with open(imagefile, "r") as f:
    for line in f:
        line = line.strip()
        labels.append(line)

for can in cans:
    print(labels[can])
