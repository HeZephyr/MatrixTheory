import numpy as np
from sympy import Matrix

'''
Full-Rank Factorization
@params: A Matrix
@return: F, G Matrix
'''
def full_rank(A):
    r = A.rank()
    A_arr1 = np.array(A.tolist())
    # 求解A的最简行阶梯矩阵，要转换成list，再转换成array
    A_rref = np.array(A.rref()[0].tolist())
    k = [] # 存储被选中的列向量的下标
    # 遍历A_rref的行
    for i in range(A_rref.shape[0]):
        # 遍历A_rref的列
        for j in range(A_rref.shape[1]):
            # 遇到1就说明找到了A矩阵的列向量的下标
            # 这些下标的列向量组成F矩阵，然后再找下一行
            if A_rref[i][j] == 1:
                k.append(j)
                break
    # 通过选中的列下标，构建F矩阵       
    B = Matrix(A_arr1[:,k])
    # G就是取行最简行矩阵A的前r行构成的矩阵
    C = Matrix(A_rref[:r])

    return B, C

if __name__ == "__main__":
    # 表示矩阵A
    A = np.array([[1, 1, 0], [0, 1, 1], [-1, 0, 0], [1, 1, 1]])
    A = Matrix(A)
    B, C = full_rank(A)
    print("B:", B)
    print("C:", C)