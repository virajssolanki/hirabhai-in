from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open('1.jpeg')
im2 = Image.open('ABHAY2.png')
#im1 = Image.open('lena.jpg')
im1 = im1.resize(im2.size)

mask = Image.open('mask.png').convert('L').resize(im2.size)
im = Image.composite(im1, im2, mask)
im.save('ball.png')

#ironman = im1
#bg = im2
#text_img = Image.new('RGBA', (600,320), (0, 0, 0, 0))
#text_img.paste(bg, (0,0))
#text_img.paste(ironman, (0,0), mask=ironman.split()[1])
#text_img.save("ball.png", format="png")