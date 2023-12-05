import numpy as np
from sympy import Matrix
import pprint

A = np.array([[1,0],[0,1],[1,1]])
# 求A的奇异值分解
U, sigma, VT = np.linalg.svd(A)
print ("U:", U)
print ("sigma:", sigma)
print ("VT:", VT)