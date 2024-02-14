def gcd(a, b):

    if a > b:
        a, b = b, a

    while a != 0:
        print(b, a)
        b, a = a, b % a
        print(b, a)

    return b


a = 66528
b = 52920

print(gcd(17, 5))
