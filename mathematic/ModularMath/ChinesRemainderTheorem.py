def chinesThorem(m, r):
    M = 1
    for i in m:
        M *= i

    result = 0

    for i, j in zip(m, r):
        Mi = M // i
        alpha = pow(Mi, -1, i)
        result += j*alpha*Mi
        result %= M

    return result


modulus = [5, 11, 17]
remainders = [2, 3, 5]
print(chinesThorem(modulus, remainders))
