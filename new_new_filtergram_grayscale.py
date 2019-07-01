from grayscale import *

img = load_image('bluerainbow.jpg')
img_3 = rainbow(img)
save_image(img_3, 'bluerainbowfilter.jpg')


