import numpy as np

def manhattan(a, b):
   a =np.asarray(a)
   b =np.asarray(b)
   return np.sum(np.abs(a-b))

def euclidean(a, b):
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]

    distance = np.sqrt(d_x**2 + d_y**2)
    return distance
