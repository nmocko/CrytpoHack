from Crypto.Cipher import AES
import hashlib

with open("./words") as f:
    words = [w.strip() for w in f.readlines()]

ct = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

for word in words:

    KEY = hashlib.md5(word.encode()).digest()

    cipher = AES.new(KEY, AES.MODE_ECB)
    decrypted = cipher.decrypt(bytes.fromhex(ct))

    if decrypted.startswith(b'crypto{'):
        print(decrypted.decode())
