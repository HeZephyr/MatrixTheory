import numpy as np
from sympy import symbols, Matrix
import pprint


# 定义符号变量
lambda_ = symbols('lambda')

A = np.array([[0, 2, 1], [-2, 0, 3], [-1, -3, 0]])
A = Matrix(A)

# 求特征矩阵
characteristic_matrix = A - lambda_ * np.eye(3)
pprint.pprint("关于 lambda 的特征矩阵:")
pprint.pprint(characteristic_matrix)

# 计算特征多项式
characteristic_polynomial = A.charpoly(lambda_)
pprint.pprint("关于 lambda 的特征多项式:")
pprint.pprint(characteristic_polynomial)

# 求特征值
eigenvalues = A.eigenvals()
# 打印特征值、其代数重数、特征向量和几何重数

for k, v in eigenvalues.items():
    pprint.pprint("特征值 %s 的代数重数为 %s" % (k, v))
    pprint.pprint("特征值 %s 的几何重数为 %s" % (k, A.eigenvects()[list(eigenvalues.keys()).index(k)][1]))
    pprint.pprint("特征值 %s 的特征向量为 %s" % (k, A.eigenvects()[list(eigenvalues.keys()).index(k)][2]))
    
# 判断A是否可对角化，如果可以，打印出对角化矩阵
if A.is_diagonalizable():
    pprint.pprint("A可对角化")
    pprint.pprint("对角化矩阵为:")
    pprint.pprint(A.diagonalize()[0])

# 求A的行空间、列空间、零空间
pprint.pprint("A的行空间为:")
pprint.pprint(A.rowspace())
pprint.pprint("A的列空间为:")
pprint.pprint(A.columnspace())
pprint.pprint("A的零空间为:")
pprint.pprint(A.nullspace())