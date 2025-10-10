def xor_text(text):
    # turn the string into a list 
    # make each charatcer unicode
    word = list(text)
    unicode = []
    for w in word:
        w = ord(w)
        unicode.append(w) 

    xored = 13
    code = []
    for u in unicode:
        u = u ^ xored
        code.append(u)
    
    decoded = []
    for c in code:
        c = chr(c)
        decoded.append(c)
    decoded = ''.join(decoded)
    print(f"The dexoded XOR string is: {decoded}")

def xor_bytes():
    # Get list of hex values from user
    user_input = input("Enter bytes to decode (comma separated hex values, e.g. 0x8484d893, 0x97c6c390):\n")
    values_str = user_input.strip().split(',')
    values = [int(v.strip(), 16) for v in values_str if v.strip()]

    # Get xor value from user
    xor_value = int(input("Enter the byte XOR key (e.g. 0xa5a5a5a5):\n").strip(), 16)

    # Decode
    flag = []
    for val in reversed(values):
        xored = val ^ xor_value
        bytes_val = xored.to_bytes(4, 'little')
        # Use errors='replace' in case of non-ASCII output
        result = bytes_val.decode('ascii', errors='replace')
        flag.append(result)

    print(''.join(flag))
