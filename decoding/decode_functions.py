# Each function has it's own Import

def ascii():
    solution = []
    code = input("Enter ASCII string to decode: ")
    # Split string into a list and iterate
    for c in code.split():
        c = int(c)
        solution.append(chr(c))
    # Join decoded letters into a string
    decoded = (''.join(solution))
    return decoded

def octal():
    # Converts a string of octal numbers to plain text
    code = input("Enter Octal string to decode: ")
    # Split the input by spaces and convert each number from octal, then turn to character
    decoded = ''.join(chr(int(oct_num, 8)) for oct_num in code.split())
    return decoded

def hex():
    code = input("Enter Hex string to decode: ")
    # Convert from Hex using bytes.fromhex()
    encoded = bytes.fromhex(code)
    # strip the "b'text' encoding"
    decoded = encoded.decode()
    print(decoded)

def base64():
    import base64
    code = input("Enter base64 string to decode: ")
    decoded = base64.b64decode(code).decode()
    print(decoded)

def base85():
    import base64
    code = input("Enter base85 encoded text: ")
    data = code.replace("\n","")
    encoded = data
    print(base64.a85decode(encoded))

def decode_base65536():
    import base65536
    code = input("Enter Base65536 encoded text: ")
    return base65536.decode(code)

def qr_code(): #for inception
    from pyzbar.pyzbar import decode
    from PIL import Image
    code = input("Enter the name of the QR.png file: ")
    img = Image.open(code)
    result = decode(img)
    for d in result:
        print(d.data.decode())
