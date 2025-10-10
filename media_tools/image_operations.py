# RGB is made up up 3 variables's (R, G, & B) with values between 0-256
# Use Pillow for working with the file format compleixty (Image, wav, etc)

from PIL import Image

flag_img = Image.open('flag_7ae18c704272532658c10b5faad06d74.png')
lemur = Image.open('lemur_ed66878c338e662d3473f0d98eedbd0d.png')

print(f"Flag img size: {flag_img.size}, mode: {flag_img.mode}")
print(f"Lemur img size: {lemur.size}, mode: {lemur.mode}")

flag_pixels = list(flag_img.getdata())
lemur_pixels = list(lemur.getdata())

print(f"First Flag pixel: {flag_pixels[0]}")
print(f"First Lemur pixel: {lemur_pixels[0]}")

flag_rgb_bytes = flag_img.tobytes()
lemur_rgb_bytes = lemur.tobytes()

print(f"First Flag 9 bytes: {flag_rgb_bytes[:9]}")
print(f"First Lemur 9 bytes: {lemur_rgb_bytes[:9]}")

xored_rgb_bytes = bytes([f ^ l for f, l in zip(flag_rgb_bytes, lemur_rgb_bytes)])

flag = Image.frombytes('RGB', (582, 327), xored_rgb_bytes)
flag.save('flag.png')
