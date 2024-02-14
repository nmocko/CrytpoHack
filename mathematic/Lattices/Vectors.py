import numpy as np

v = [2, 6, 3]
w = [1, 0, 0]
u = [7, 7, 2]

vv = np.array(v)
vw = np.array(w)
vu = np.array(u)

v1 = 3*(2*vv - vw)
v2 = 2*vu
print(v1.dot(v2))

# calculate 3*(2*v - w) ∙ 2*u.

