def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n < x:
        high *= 2
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1


import math
from Crypto.Util.number import long_to_bytes, bytes_to_long

ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957


flag = find_invpow(ct, 3)
print(flag)
# flag += 10000000000000000000000000000000000000000
f = int(round(flag))
print('difference', ct - pow(f, 3))
print(int(flag))
print(long_to_bytes(int(flag)))

flag = b"cryptoXXXXXXXXXXXXXXXXX"

print(bytes_to_long(flag))
x = bytes_to_long(flag)
print(pow(x, 3))
