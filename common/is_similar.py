import numpy as np
import pprint
from sympy import Matrix


'''
判断两个矩阵是否相似
@param A: Matrix A
@param B: Matrix B
@return: True or False
'''
def is_similar(A, B):
    # 判断是否具有相同的Jordan标准形
    if A.jordan_form() != B.jordan_form():
        return False
    return True

if __name__ == "__main__":
    A = np.array([[0, 2, 1], [-2, 0, 3], [-1, -3, 0]])
    A = Matrix(A)
    B = np.array([[1, 1, 0], [0, 1, 1], [-1, 0, 0]])
    B = Matrix(B)
    pprint.pprint("A:")
    pprint.pprint(A)
    pprint.pprint("B:")
    pprint.pprint(B)
    pprint.pprint("A和B是否相似:")
    pprint.pprint(is_similar(A, B))
    # A:
    # Matrix([[0, 2, 1], [-2, 0, 3], [-1, -3, 0]])
    # B:
    # Matrix([[1, 1, 0], [0, 1, 1], [-1, 0, 0], [1, 1, 1]])
    # A和B是否相似:
    # True