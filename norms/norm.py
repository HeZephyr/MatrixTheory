import numpy as np

A = np.matrix([[-1, -1, 4], [1, 1, 2], [1, -2, 2]])

# 表示复数矩阵[[1, -1, 1], [-i, 0, 2i], [1, 1, 1]]
B = np.matrix([[1, -1, 1], [-1j, 0, 2j], [1, 1, 1]])

# 求A的矩阵范数，ord分别为1，2，np.inf，F
print("A范数")
print("A的1范数（列和范数）：", np.linalg.norm(A, ord=1))
print("A的2范数（谱范数）：", np.linalg.norm(A, ord=2))
print("A的无穷范数（行和范数）：", np.linalg.norm(A, ord=np.inf))
print("A的F范数：", np.linalg.norm(A, ord='fro'))

print("B范数")
print("B的1范数（列和范数）：", np.linalg.norm(B, ord=1))
print("B的2范数（谱范数）：", np.linalg.norm(B, ord=2))
print("B的无穷范数（行和范数）：", np.linalg.norm(B, ord=np.inf))
print("B的F范数：", np.linalg.norm(B, ord='fro'))