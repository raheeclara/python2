import csv
import numpy as np
import matplotlib.pyplot as plt

f = open('class.csv')
data = csv.reader(f)

h = next(data)
w = next(data)

h = np.array(h[2:],dtype = int)
w = np.array(w[2:],dtype = int)

for row in data :
    if '키' in row[1:] :
        h = np.concatenate((h,np.array(row[2:],dtype = int)), axis = None)
    if '몸무게' in row [1:]:
        w = np.concatenate((w,np.array(row[2:],dtype = int)), axis = None)

plt.scatter(h,w,c = w,cmap = 'jet')
plt.colorbar()
plt.show()
