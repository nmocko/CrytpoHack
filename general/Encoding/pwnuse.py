import codecs

from Crypto.Util.number import long_to_bytes
from pwn import *
import json

r = remote('socket.cryptohack.org', 13377, level='debug')


def json_recv():
    ans = r.recvline()
    return json.loads(ans.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(100):

    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    answer = ""

    if received["type"] == "base64":
        answer = base64.b64decode(received["encoded"])
    elif received["type"] == "hex":
        answer = bytes.fromhex(received["encoded"])
    elif received["type"] == "rot13":
        answer = codecs.decode(received["encoded"], 'rot13')
    elif received["type"] == "bigint":
        answer = long_to_bytes(int(received["encoded"], 16)).decode()
    elif received["type"] == "utf-8":
        for b in received["encoded"]:
            answer += chr(b)
    else:
        answer = "We have a problem"

    print(answer)

    to_send = {
        "decoded": answer
    }
    json_send(to_send)

    json_recv()
