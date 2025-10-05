from pwn import * # pip install pwntools
import json
import base64
from Crypto.Util.number import long_to_bytes

# Use Pwntools and PyCryptodome to repeat a request for encoded text, decoding until a flag is hit
# Must set the HOST, PORT, and flag_text variables

# ======== Receiving the encypted Text ========

HOST = 'socket.cryptohack.org'
PORT = 13377


r = remote(HOST, PORT, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


# ======== Functions for different encodings ========

def ascii():
    solution = []
    code = received["encoded"]
    for c in code:
        solution.append(chr(c))
    decoded = (''.join(solution))
    return decoded

def hex():
    code = received["encoded"]
    encoded = bytes.fromhex(code)
    decoded = encoded.decode()
    return decoded

def base():
    code = received["encoded"]
    decoded = base64.b64decode(code).decode()
    return decoded

def rot13():
    table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
    code = received["encoded"]
    decoded = code.translate(table)
    return decoded

def bigint():
    code = received["encoded"]
    encoded = int(code, 16)
    decoded = long_to_bytes(encoded)
    return decoded.decode()


# Loop through the encryptions until we get the flag

while True:
    received = json_recv()
    flag_text = 'flag'

    if flag_text in received:
        print('FLAG:',received["flag"])
        break

    elif received["type"] == 'utf-8': 
        to_send = {
            "decoded": ascii()
        }
        json_send(to_send)
        

    elif received["type"] == 'hex': 
        to_send = {
            "decoded": hex()
        }
        json_send(to_send) 

    elif received["type"] == 'base64': 
        to_send = {
            "decoded": base()
        }
        json_send(to_send) 

    elif received["type"] == 'rot13': 
        to_send = {
            "decoded": rot13()
        }
        json_send(to_send) 
        
    elif received["type"] == 'bigint': 
        to_send = {
            "decoded": bigint()
        }
        json_send(to_send) 
        
    else:
        pass
    



