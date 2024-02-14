import numpy as np


def GramSchmist(v, l, orthonormal=1):

    for i in range(l):
        for j in range(i):
            uij = (v[i].dot(v[j])) / (np.linalg.norm(v[j]) ** 2)
            v[i] = v[i] - uij * v[j]

    if orthonormal == 1:
        for i in range(l):
            ll = np.linalg.norm(v[i])
            v[i] = v[i] / ll

    return v


v = [np.array([4, 1, 3, -1]), np.array([2, 1, -3, 4]), np.array([1, 0, -2, 7]), np.array([6, 2, 9, -5])]
l = len(v)

print(GramSchmist(v, l, 0))
