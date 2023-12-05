import numpy as np
from sympy import Matrix
import pprint

A = np.array([[2, 2, 1], [-2, 6, 1], [0, 0, 4]])
A = Matrix(A)
P, J = A.jordan_form()
# 验证P^-1 * A * P = J
assert P ** -1 * A * P == J, "P^-1 * A * P != J"
pprint.pprint("P:", P)
pprint.pprint("J:", J)