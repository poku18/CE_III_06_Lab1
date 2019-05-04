from lab1 import linearSearch
from lab1 import binarySearch
import random
from time import time
import matplotlib.pyplot as plt

n = 100000
i = 0
timeArrayLinear = []
timeArrayBinary = []
sizeArray = []

#timing linear search
for i in range(n, n * 11, n):
	sizeArray.append(i)
	randomvalues = random.sample(range(i), i)
	startTime = time()
	linearSearch(randomvalues, randomvalues[i-1])
	endTime = time()
	totalTime = endTime - startTime
	timeArrayLinear.append(totalTime)
	print(totalTime, "for size", i)

n = 100000
i = 0

# timing binary search
for i in range(n, n * 11, n):
	randomvalues = random.sample(range(i),i)
	startTime = time()
	binarySearch(randomvalues, randomvalues[i-1])
	endTime = time()
	totalTime = endTime - startTime
	timeArrayBinary.append(totalTime)
	print(totalTime, "for size", i)

# draw graph for time vs size for both algorithms
fig, ax = plt.subplots(1, 1)
ax.plot(sizeArray,timeArrayLinear, label = 'Linear Search')
ax.plot(sizeArray,timeArrayBinary, label = 'Binary Search')
legend = ax.legend(loc = 'upper center', shadow = True, fontsize = 'large')
plt.show()
