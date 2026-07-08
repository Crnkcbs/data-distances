import numpy as np

def minkowski(a, b, p):
    a = np.asarray(a)
    b = np.asarray(b)
    # Genel Minkowski formülü
    return np.sum(np.abs(a - b) ** p) ** (1 / p)

def manhattan(a, b):
    # Manhattan aslında p=1 olan Minkowski'dir!
    return minkowski(a, b, p=1)

def euclidean(a, b):
    # Öklid aslında p=2 olan Minkowski'dir!
    return minkowski(a, b, p=2)
