def egcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = egcd(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y




b = 26513
a = 32321

print(egcd(5, 17))

