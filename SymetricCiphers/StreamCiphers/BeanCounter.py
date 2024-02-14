plaintext01 = bytes.fromhex('89504e470d0a1a0a0000000d49484452')

with open("/home/reny/imageecb", 'r') as f:
    with open('/home/reny/image.png', 'wb') as image:
        block = f.read(32)
        key = bytes(a ^ b for a, b in zip(bytes.fromhex(block), plaintext01))

        while block:
            plaintext = bytes(a ^ b for a, b in zip(bytes.fromhex(block), key))
            image.write(plaintext)
            block = f.read(32)
