from PIL import Image, ImageFilter, ImageDraw
import numpy as np
import itertools

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
# im1 = Image.open('data/src/rocket.jpg')
# im2 = Image.open('data/src/lenna_square.png')
#
# back_im = im1.copy()
# back_im.paste(im2)
# back_im.save('data/dst/rocket_pillow_paste.jpg', quality=95)
#
# # 位置を指定して貼り付け
# back_im = im1.copy()
# back_im.paste(im2, (100, 50))
# back_im.save('data/dst/rocket_pillow_paste_pos.jpg', quality=95)
#
# # マスク画像を利用
# mask_im = Image.new("L", im2.size, 0)
# draw = ImageDraw.Draw(mask_im)
# draw.ellipse((140, 50, 260, 170), fill=255)
# mask_im.save('data/dst/mask_circle.jpg', quality=95)
#
# back_im = im1.copy()
# back_im.paste(im2, (0, 0), mask_im)
# back_im.save('data/dst/rocket_pillow_paste_mask_circle.jpg', quality=95)
#
# # マスクをぼかす
# mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(10))
# mask_im_blur.save('data/dst/mask_circle_blur.jpg', quality=95)
#
# back_im = im1.copy()
# back_im.paste(im2, (0, 0), mask_im_blur)
# back_im.save('data/dst/rocket_pillow_paste_mask_circle_blur.jpg', quality=95)

# フィルタ
# im = np.array(Image.open('data/src/lenna_square.png'))
# print(type(im))
# print(im.dtype)
# print(im.shape)
# print(im[0, 0])
# R, G, B = im[10, 10]
# pil_img = Image.fromarray(im)
im = np.array((Image.open('data/src/lenna_square.png')).convert('L'))
print(type(im))
print(im.dtype)
print(im.shape)
range_X = im.shape[0]
range_Y = im.shape[1]
print(range_X)
print(range_Y)
im_new = np.zeros((range_X, range_Y), dtype=int)
# filter = np.full((3, 3), 1 / 9)
filter = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])
theta = 15
cos_theta = np.cos(np.radians(theta))
sin_theta = np.sin(np.radians(theta))
array = np.array([[cos_theta, -sin_theta],
                  [sin_theta, cos_theta]])
# for i, j in itertools.product(range(1, range_X - 1), range(1, range_Y - 1)):
#     checked_array = im[i - 1:i + 2, j - 1:j + 2]
#     filtered_array = filter * checked_array
#     sum_value = np.sum(filtered_array)
#     im_new[i][j] = sum_value
for i, j in itertools.product(range(range_X), range(range_Y)):
    x_old, y_old = i, j
    [x_new, y_new] = array @ [x_old, y_old]
    x_new, y_new = int(x_new), int(y_new)
    if x_new in range(0, range_X) and y_new in range(0, range_Y):
        im_new[x_new, y_new] = im[x_old, y_old]

pil_img = Image.fromarray(im_new)
pil_img.show()
# pil_img.save('data/temp_lena_save_pillow.jpg')
