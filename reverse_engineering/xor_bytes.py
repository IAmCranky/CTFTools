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
