import base64
from capstone import *
import binascii


ciphertext = base64.b64decode('zGdgT6GHR9uXJ682kdam1A5TbvJP/Ap87V6JxICzC9ygfX2SUoIL/W5cEP/xekJTjG+ZGgHeVC3clgz9x5X5mgWLGNkga+iixByTBkka0xbqYs1TfOVzk2buDCjAesdisU887p9URkOL0rDve6qe7gjyab4H25dPjO+dVYkNuG8wWQ==')
key = base64.b64decode('me6Fzk0HR9uXTzzuFVLORM2V+ZqMbA==')

def xor_decrypt(ciphertext_bytes, key_bytes):
    decrypted_bytes = bytearray()
    key_length = len(key_bytes)
    for i, byte in enumerate(ciphertext_bytes):
        decrypted_bytes.append(byte ^ key_bytes[i % key_length])
    return bytes(decrypted_bytes)

plaintext = xor_decrypt(ciphertext, key)
print(plaintext.hex())

hexcode = plaintext.hex()
code = binascii.unhexlify(hexcode)


# Create disassembler
md = Cs(CS_ARCH_X86, CS_MODE_32)
md.syntax = CS_OPT_SYNTAX_INTEL

# Disassemble
for i in md.disasm(code, 0x1000):
    print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))

