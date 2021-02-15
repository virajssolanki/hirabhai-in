from PIL import Image, ImageDraw

img = Image.new('RGB', (100, 30), color = (73, 109, 137))
im = Image.open("images/img.png")
im.show()

d = ImageDraw.Draw(img)
d.text((10,10), "Hello World", fill=(255,255,24))
 
img.save('pil_text.png')