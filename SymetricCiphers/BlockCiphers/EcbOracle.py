import requests

space = ''

for i in range(33, 127):
    space += chr(i)

print(space)

flag = ''

for i in range(25):

    pt = '00' * (31 - i)
    r = requests.get(f'https://aes.cryptohack.org/ecb_oracle/encrypt/{pt}/')
    ct = r.json()['ciphertext'][:64]

    for f in space:

        text = pt + flag + format(ord(f), "x")
        r = requests.get(f'https://aes.cryptohack.org/ecb_oracle/encrypt/{text}/')

        if r.json()['ciphertext'][:64] == ct:
            flag += format(ord(f), "x")
            break

print(bytes.fromhex(flag).decode())

