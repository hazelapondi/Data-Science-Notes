import numpy as np

#generate random samples
height = np.round(np.random.normal(1.75,0.20,5000),2)
weight = np.round(np.random.normal(60.32,15,5000),2)

#use column stack to paste them together
np_city = np.column_stack((height,weight))

#perform a sanity check by getting the mean and median
np.mean(np_city[:,0]) #tells Python to get all the rows, and the first column
np.median(np_city[:,0])

#to check if height or weight are correlated
np.corrcoef(np_city[:,0],np_city[:,1])

np.std(np_city[:,0])

#numpy enforces single data type so it drastically speeds up the calculations

np.median(np_city[:,1]) #tells Python to get all the rows, and the second column


#numpy tutorial:http://www.numpy.org/