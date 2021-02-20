from PIL import Image, ExifTags, ImageOps

img = Image.open('ball.png')
#fixed_image = ImageOps.exif_transpose(img)
#fixed_image.save("ball.png", format="png")
img_exif = img.getexif()
image_orientation = img_exif[274]
print(image_orientation)
#img_exif_dict = dict(img_exif)
    # { ... 42035: 'FUJIFILM', 42036: 'XF23mmF2 R WR', 42037: '75A14188' ... }
#for key, val in img_exif_dict.items():
#    if key in ExifTags.TAGS:
#        print(f"{ExifTags.TAGS[key]}:{repr(val)}")

#print(img._getexif())
#exif=dict((ExifTags.TAGS[k], v) for k, v in img._getexif().items() if k in ExifTags.TAGS)
#if not exif['Orientation']:
#    img=img.rotate(90, expand=True)
#img.thumbnail((1000,1000), Image.ANTIALIAS)
#img.save(output_fname, "JPEG")











#from PIL import Image, ImageDraw, ImageFilter

#im1 = Image.open('1.jpeg')
#im2 = Image.open('ABHAY2.png')
#im1 = Image.open('lena.jpg')
#im1 = im1.resize(im2.size)

#mask = Image.open('mask.png').convert('L').resize(im2.size)
#im = Image.composite(im1, im2, mask)
#im.save('ball.png')

#ironman = im1
#bg = im2
#text_img = Image.new('RGBA', (600,320), (0, 0, 0, 0))
#text_img.paste(bg, (0,0))
#text_img.paste(ironman, (0,0), mask=ironman.split()[1])
#text_img.save("ball.png", format="png")