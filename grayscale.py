import math 
from PIL import Image

def load_image(filename): 
    image = Image.open(filename)
    return image

def show_image(img): 
    img.show()

def save_image(img, filename):
    img.save(filename)

def rainbow(img): 
    data = img.getdata()
    n_data = []
    
    
    for pixel in data: 
        photo_intensity = (pixel[0] + pixel[1] + pixel[2])//3
        n_data.append((photo_intensity,photo_intensity,pixel[0]))

    new_image = Image.new("RGB", img.size)
    new_image.putdata(n_data)

    return new_image