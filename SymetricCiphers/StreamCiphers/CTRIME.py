import requests

space = ''

flag = '63727970746f7b'
i = 0

while True:

    min_len = 10000
    f = '00'
    for s in range(33, 127):
        text = flag[i: i+14] + f'{s:X}'
        r = requests.get(f'https://aes.cryptohack.org/ctrime/encrypt/{text}/')
        len_ct = len(r.json()['ciphertext'])

        if min_len > len_ct:
            min_len = len_ct
            f = f'{s:X}'

    flag += f
    i += 2
    print(flag)
    if f == '7D':
        break

print(bytes.fromhex(flag).decode())

