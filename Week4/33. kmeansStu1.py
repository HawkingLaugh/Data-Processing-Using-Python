import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten

list1 = [88.0, 74.0, 96.0,85.0]
list2 = [92.0, 99.0, 95.0,94.0]
list3 = [91.0, 87.0, 99.0,95.0]
list4 = [78.0, 99.0, 97.0,81.0]
list5 = [88.0, 78.0, 98.0,84.0]
list6 = [100.0, 95.0, 100.0,92.0]

data = np.array([list1,list2,list3,list4,list5,list6])
# calculate SD of each column
whiten = whiten(data)

# kmeans for clustering. second argument for how many groups to form
# kmeans return a tuple
# only need the first return, therefore the _ is for data dumping
centroids,_ = kmeans(whiten,2)

# put the kmeans result into vq.
# vq is a vector quantization function, may classify each data
result,_ = vq(whiten, centroids)
print(result)