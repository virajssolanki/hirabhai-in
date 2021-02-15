from PIL import Image, ImageDraw

image = Image.open("img.png")
image = image.convert('RGB')
r, g, b = image.split()  
image = Image.merge("RGB", (b, g, r))

image.save('pil_text.png')