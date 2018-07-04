import numpy as np
from numpy.lib.stride_tricks import as_strided
n = 5; k=2
a = np.linspace(1, n, n); aid = id(a)
as_strided(a, (k, n ),(8,8))
as_strided(a, (k, n-k+1 ),(8,8))
def shift1(x, k):
    return np.vstack([x[i:n-k+i+1] for i in range(k)])

def shift2(x, k):
    return as_strided(x, (k, n-k+1), (x.itemsize,)*2)

b = shift1(a,k); b, id(b) == aid
