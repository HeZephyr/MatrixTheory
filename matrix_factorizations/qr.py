import numpy as np
import sympy
from sympy import Matrix
from sympy import *
import pprint


#正交三角分解（QR）
a = [[1, 1, -1],
     [-1, 1, 1],
     [1, 1, -1],
     [1, 1, 1]]
 
# a = [[1,1,-1],
#                   [1,0,0],
#                   [0,1,0],
#                   [0,0,1]]
A_mat = Matrix(a)#α向量组成的矩阵A
# A_gs= GramSchmidt(A_mat)
A_arr = np.array(A_mat)
L = []
for i in range(A_mat.shape[1]):
    L.append(A_mat[:,i])
#求Q
A_gs = GramSchmidt(L)#α的施密特正交化得到β
A_gs_norm = GramSchmidt(L,True)#β的单位化得到v
 
A = []
 
for i in range(A_mat.shape[1]):
    for j in range(A_mat.shape[0]):
        A.append(A_gs_norm[i][j])#把数排成一行
 
A_arr = np.array(A)
A_arr = A_arr.reshape((A_mat.shape[0],A_mat.shape[1]),order = 'F')#用reshape重新排列（‘F’为竖着写）
#得到最后的Q
Q = Matrix(A_arr)
 
#求R
 
C = []
for i in range(A_mat.shape[1]):
    for j in range(A_mat.shape[1]):
        if i > j:
            C.append(0)
        elif i == j:
            t = np.array(A_gs[i])
            m = np.dot(t.T,t)
            C.append(sympy.sqrt(m[0][0]))
        else:
            t = np.array(A_mat[:,j])
            x = np.array(A_gs_norm[i])
            n = np.dot(t.T,x)
#             print(n)
            C.append(n[0][0])
# C_final为R          
C_arr = np.array(C)
# print(C_arr)
C_arr = C_arr.reshape((A_mat.shape[1],A_mat.shape[1]))
R = Matrix(C_arr)

pprint.pprint("Q:")
pprint.pprint(Q)
pprint.pprint("R:")
pprint.pprint(R)
# 求矩阵A的QR分解，保留根号
Q_, R_ = A_mat.QRdecomposition()
pprint.pprint("Q_:")
pprint.pprint(Q_)
pprint.pprint("R_:")
pprint.pprint(R_)
assert Q_ == Q, "Q_ != Q"
assert R_ == R, "R_ != R"