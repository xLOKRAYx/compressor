from PIL import Image

f = open('test.zip', 'rb')
data = f.read()
f.close()
print(data)

img = Image.new('RGB', (1920, 1080))
img.putdata(data)
img.save('image.png')
