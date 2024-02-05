from PIL import Image
img = Image.new('RGB', (1920, 1080))

chunk_size = 256
 
file = open("test.zip", "rb")
offset = 0
while True:
    chunk = file.read(chunk_size)
    if not chunk:
        break
    img.putdata(f"Read {len(chunk)} bytes: {chunk}", offset)
    offset = offset + 1

img.save('image.png')
