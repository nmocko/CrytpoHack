from Crypto.PublicKey import RSA

with open("/home/reny/Downloads/transparency.pem", "rb") as k:
    key = RSA.importKey(k.read())

print(key.n)
