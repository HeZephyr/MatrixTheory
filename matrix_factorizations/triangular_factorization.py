import numpy as np
from sympy import Matrix
import pprint

EPSILON = 1e-8

def is_zero(x):
    return abs(x) < EPSILON

def LU(A):
    # 断言A必须是非奇异方阵A
    assert A.rows == A.cols, "Matrix A must be a square matrix"
    assert A.det() != 0, "Matrix A must be a nonsingular matrix"

    n = A.rows

    U = A
    # 构建出U矩阵
    # 将U转换成list，再转换成array
    U = np.array(U.tolist())

    # 遍历U的每一行利用高斯消元法
    for i in range(n):
        # 判断U[i][i]是否为0
        assert not is_zero(U[i][i]), "主元为0，无法进行LU分解"
        # 对i+1行到n行进行消元
        for j in range(i + 1, n):
            # 计算消元因子
            factor = U[j][i] / U[i][i]
            # 对第j行进行消元
            for k in range(i, n):
                U[j][k] -= factor * U[i][k]
    # 消元后的矩阵U则是最终U矩阵
    U = Matrix(U)
    # 根据LU = A，得到L矩阵
    L = A * U.inv()
    return L, U

def LDU(A):
    L, U = LU(A)
    D = Matrix(np.diag(np.diag(U)))
    U = D.inv() * U
    return L, D, U

if __name__ == '__main__':
    A = np.array([[2, 3, 4], [1, 1, 9], [1, 2, -6]])
    A = Matrix(A)
    '''
    # test LU分解
    L, U = LU(A)
    pprint.pprint("L:")
    pprint.pprint(L)
    pprint.pprint("U:")
    pprint.pprint(U)
    '''
    # test LDU分解
    L, D, U = LDU(A)
    pprint.pprint("L:")
    pprint.pprint(L)
    pprint.pprint("D:")
    pprint.pprint(D)
    pprint.pprint("U:")
    pprint.pprint(U)