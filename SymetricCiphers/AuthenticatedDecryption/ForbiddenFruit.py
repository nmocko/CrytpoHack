from time import sleep
import random

# h = "7c61bb6c7da4dba7630dc59d407ba87b"
# #    g i v e   m e   t h e   f l a g
ad = "43727970746f4861636b000000000000"
# ct = "1b08cd095dc9be871765a0bd2617c91c"
length = "00000000000000500000000000000080"
# iv = "88276c4db3b315358d61708f"
# mod = int("80000000000000000000000000000087", 16)
mod = int("100000101", 2)


def gmul(a, b):
    p = 0

    while a > 0:
        if a & 1:
            p = p ^ b

        a = a >> 1
        b = b << 1

    return p


def gmulmod(a, b, m=mod):
    p = 0
    while a > 0:
        if a & 1:
            p = p ^ b

        a = a >> 1
        b = b << 1

        if len(str(bin(b))) == len(str(bin(m))):
            b = b ^ m

    return p


def gmod(a, b):
    q, r = 0, a

    while len(str(bin(r))) >= len(str(bin(b))) and r != 0:
        d = len(str(bin(r))) - len(str(bin(b)))
        q = q ^ (1 << d)
        r = r ^ (b << d)

    return q, r


def ginvmod(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = ginvmod(gmod(b, a)[1], a)

    x = y1 ^ gmul((gmod(b, a)[0]), x1)
    y = x1

    return gcd, x, y


def ggcd(a, b):

    if a > b:
        a, b = b, a

    while a != 0:
        tmp = gmod(b, a)
        b = a
        a = tmp[1]

    return b


def g_power(a, b, f):

    y = 1
    while b > 1:
        if b % 2 == 1:
            y = gmulmod(a, y, f)
            b = b - 1
        a = gmulmod(a, a, f)
        b = b // 2
    return gmulmod(a, y, f)


def g_square_root(c, exponent_of_gf2):

    r = c
    for i in range(exponent_of_gf2 - 1):
        r = gmulmod(r, r)

    return r

def gderivative(f):
    return (f >> 1) & int("01" * (len(str(bin(f))) + 1), 2)


def square_free_factorization(f, p, recursion):
    r = []

    f_prim = gderivative(f)
    c = ggcd(f, f_prim)
    print(c)
    w = gmod(f, c)[0]

    i = 1
    while w != 1:
        y = ggcd(w, c)
        print('y', y)
        fac = gmod(w, y)[0]
        print('fac', fac)
        if fac != 1:
            if recursion != 0:
                r.append([fac, p**recursion])
            else:
                r.append([fac, i])
        w = y
        c = gmod(c, y)[0]
        i = i + 1

    if c != 1:
        print('oh no')
        c = g_square_root(c, 128 * 128 * 128)
        for i in square_free_factorization(c, p, recursion + 1):
            r.append(i)

    return r


def distinct_degree_factorization(f):
    i = 1
    S = []
    f_prim = f

    polynomial = 2

    while len(str(bin(f_prim))) - 2 >= 2 * i and len(str(bin(f_prim))) - 2 != 0:
        polynomial = gmulmod(polynomial, polynomial, f_prim)
        g = ggcd(f_prim, polynomial ^ 2)
        if g != 1:
            S.append([g, i])
            f_prim = gmod(f_prim, g)[0]
            polynomial = gmod(polynomial, f_prim)[1]
        i += 1

    if f_prim != 1:
        S.append([f_prim, len(str(bin(f_prim))) - 2])
    if not S:
        return [f, 1]
    else:
        return S


def equal_degree_factorization(f, d):
    n = len(str(bin(f))) - 2
    r = n // d
    S = [f]
    power = (2**d - 1)//3

    # to do: test redukowalności
    if f == 3:
        return [3]
    if f == 2:
        return [2]

    while len(S) < r:
        h = random.randint(1, f)
        g = ggcd(h, f)

        if g == 1:
            g = gmod(g_power(h, power, f) ^ 1, f)[1]

        for u in S:
            if len(str(bin(u))) == d:
                continue

            t = ggcd(g, u)
            if t != 1 and t != u:
                S.remove(u)
                S.append(t)
                S.append(gmod(u, t)[0])

    return S

a = 10
for i in range(mod + 2):
    b = g_power(a, i, mod)
    if b == a:
        print(i)
print('================================')

for i in range(mod + 1):
    b = g_power(i, 241, mod)
    if b != i:
        print(i, b)

# tag1 = "a057b013bd0b18d3b5ed86edced628ff"
# ct1 = "170ecf0712d0b0c81766aae92b14dc4e"
# ct1_inv = str(bin(ginvmod(int(ct1, 16), mod)[1]))[2:]
# ct1_inv = '0' * (128 - len(ct1_inv)) + ct1_inv
# dla "kotkotkotkotkot5"

tag1 = "aa5eff51fb9db6e6e41f2fb5fb1055f1"
ct1 = "170ed8041cc9fbd40d64a0fa60479b5b"
# ct2_inv = str(bin(ginvmod(int(ct2, 16), mod)[1]))[2:]
# ct2_inv = '0' * (128 - len(ct2_inv)) + ct2_inv
# dla "kocham snieg <3 "

tag2 = "dfc9a17e496ecb9269e1405208320c49"
ct2 = "1341d8035dc7b3c80777aca27f449744"
# # dla "o co chodzi?????"
# ct2_inv = str(bin(ginvmod(int(ct2, 16), mod)[1]))[2:]
# ct2_inv = '0' * (128 - len(ct2_inv)) + ct2_inv

#

# big_tag_1 = ad + ct1 + length + tag1
# big_tag_2 = ad + ct2 + length + tag2
#
# ct_inv = ginvmod(gmulmod(int(ct1, 16), int(ct2, 16)), mod)[1]
#
# tag = int(big_tag_1, 16) ^ int(big_tag_2, 16)
# tag = gmul(tag, ct_inv)
# print(bin(tag))
# print('binary', int(1010000010010100111101000010010001101001011010101110001101010101000111110010101010010101100000110101110001100111110100001110))
# print(int(big_tag_2, 16))
#
# sff = square_free_factorization(tag, 2, 0)
# print('sff', sff)
#
# ddf_sum = []
# for tab in sff:
#     ddf = distinct_degree_factorization(tab[0])
#     print('ddf', ddf)
#     for i in ddf:
#         ddf_sum.append(i)
#
# print('ddf_sum', ddf_sum)
#
# for tab in ddf_sum:
#     print('edf', equal_degree_factorization(tab[0], tab[1]))

# print(bin(786735876021320232294614529622139749))
# print(len(bin(786735876021320232294614529622139749)) - 2)
#
#
# h = 786735876021320232294614529622139749
#
# gcm = [ad, tag1, ]

# 9323872402799621453625274544294765
# 786735876021320232294614529622139749

