from Crypto.Util.number import bytes_to_long
from pwn import *
import json

r = remote('socket.cryptohack.org', 13399)  # , level='debug'
ct_token = "61" * 28
password = "a" * 8


def json_recv():
    ans = r.recvline()
    return json.loads(ans.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


r.recvline()
i = 0

while True:
    i += 1
    to_send = {
        "option": "reset_password",
        "token": ct_token
    }

    json_send(to_send)
    json_recv()

    to_send = {
        "option": "authenticate",
        "password": password
    }

    json_send(to_send)
    recived = json_recv()

    if recived["msg"] == "Wrong password.":
        to_send = {
            "option": "reset_connection"
        }

        json_send(to_send)
        json_recv()
    else:
        print(i)
        print(recived["msg"])
        break
