from PIL import Image, ImageFilter, ImageDraw
import numpy as np

# im = Image.open('data/src/lenna_square.png')
# print(im.format, im.size, im.mode)
# print(im.getextrema())
# print(im.getpixel((256, 256)))
# new_im = im.convert('L').rotate(90).filter(ImageFilter.GaussianBlur())
# print(new_im.format, new_im.size, new_im.mode)
# print(new_im.getextrema())
# print(new_im.getpixel((256, 256)))
# new_im.show()
# new_im.save('data/src/lenna_square_pillow.jpg', quality=95)
# print(im.show())
#
# im = np.array(Image.open('data/src/lenna_square.png'))
# print(type(im))
# print(im.dtype)
# print(im.shape)

# 画像の貼り付け
im1 = Image.open('data/src/rocket.jpg')
im2 = Image.open('data/src/lenna_square.png')

back_im = im1.copy()
back_im.paste(im2)
back_im.save('data/dst/rocket_pillow_paste.jpg', quality=95)

# 位置を指定して貼り付け
back_im = im1.copy()
back_im.paste(im2, (100, 50))
back_im.save('data/dst/rocket_pillow_paste_pos.jpg', quality=95)

# マスク画像を利用
mask_im = Image.new("L", im2.size, 0)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((140, 50, 260, 170), fill=255)
mask_im.save('data/dst/mask_circle.jpg', quality=95)

back_im = im1.copy()
back_im.paste(im2, (0, 0), mask_im)
back_im.save('data/dst/rocket_pillow_paste_mask_circle.jpg', quality=95)

# マスクをぼかす
mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(10))
mask_im_blur.save('data/dst/mask_circle_blur.jpg', quality=95)

back_im = im1.copy()
back_im.paste(im2, (0, 0), mask_im_blur)
back_im.save('data/dst/rocket_pillow_paste_mask_circle_blur.jpg', quality=95)