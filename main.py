from PIL import Image
img = Image.new('RGB', (1920, 1080))

chunk_size = 2
 
file = open("test.zip", "rb")
offset = 0
while True:
    chunk = file.read(chunk_size)
    if not chunk:
        break
    img.putdata(chunk, offset)
    offset = offset + chunk_size
img.save('image.png')