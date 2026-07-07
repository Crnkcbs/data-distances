import numpy as np

def manhattan(a, b):
   a =np.asarray(a)
   b =np.asarray(b)
   return np.sum(np.abs(a-b))
