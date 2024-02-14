from cmath import sqrt

import numpy as np
from Crypto.Util.number import long_to_bytes

def norm(v):
    # print(pow(v[0]*v[0] + v[1]*v[1], 1/2))
    return pow(v[0]*v[0] + v[1]*v[1], 1/2)

def GaussianLatticeReduction(v, u):

    while True:
        print('A')
        # if np.linalg.norm(u) < np.linalg.norm(v):
        #     # print('A')
        #     v, u = u, v
        m = (v.dot(u)) / (v.dot(v))
        # print(v, u, m)
        m = round(m)
        if m == 0:
            return v, u

        v, u = u - m*v, v


if __name__ == "__main__":
    v1 = np.array([846835985, 9834798552])
    u1 = np.array([87502093, 123094980])
    v2, u2 = GaussianLatticeReduction(v1, u1)
    print("dot:", v2.dot(u2))
