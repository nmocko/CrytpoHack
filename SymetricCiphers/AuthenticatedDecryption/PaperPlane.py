import requests


def xor_blocks(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


ct_1 = "7e05f59cf77ce0bb0f764e3f94f4a445"
m0 = "142d611a50cd1a3ae2f139d2fb0d76d4"
c0 = "ea224537ca154be3799218e156167740"
c0_prime = "00"
ends = ''
end = []

# for j in range(1, 17):
#     print(j, ends)
#     for i in range(256):
#         send_c0 = c0_prime * (16 - j) + f'{i:0>2X}' + ends
#
#         r = requests.get(f'https://aes.cryptohack.org/paper_plane/send_msg/{ct_1}/{m0}/{send_c0}/')
#
#         if "msg" in r.json():
#             ends = f'{i:0>2X}' + ends
#             print(ends)
#             end.insert(0, i)
#             ends = ''
#             for k in range(len(end)):
#                 t = end[k]
#                 end[k] = t ^ j ^ (j+1)
#                 ends += f'{end[k]:0>2X}'
#             break

# Found variable ends in previous loop
ends = "99402C57AE6A209B5AEE64C11972543C"
pad = "10" * 16

m1 = xor_blocks(bytes.fromhex(ends), xor_blocks(bytes.fromhex(pad), bytes.fromhex(c0))).decode()

m1_hex = bytes(m1, 'ascii').hex()
ct_2 = "ea448eb6d1e406512bbf3852c1fb2e9d"

ends = ''
end = []

# for j in range(1, 17):
#     print(j, ends)
#     for i in range(256):
#         send_c0 = c0_prime * (16 - j) + f'{i:0>2X}' + ends
#
#         r = requests.get(f'https://aes.cryptohack.org/paper_plane/send_msg/{ct_2}/{m1_hex}/{send_c0}/')
#
#         if "msg" in r.json():
#             ends = f'{i:0>2X}' + ends
#             print(ends)
#             end.insert(0, i)
#             ends = ''
#             for k in range(len(end)):
#                 t = end[k]
#                 end[k] = t ^ j ^ (j+1)
#                 ends += f'{end[k]:0>2X}'
#             break

# Found variable ends in previous loop
ends = '5D7297B88A11FAA1156C54258EEEBE5F'

m2 = xor_blocks(bytes.fromhex(ends), xor_blocks(bytes.fromhex(pad), bytes.fromhex(ct_1))).decode()

print(m1 + m2)
