p = 29
ints = [14, 6, 11]
l = len(ints)

for i in range(p):
    x = (i*i) % p
    for j in range(l):
        if x == ints[j]:
            print(i, "^ 2 % 29 =", x)
