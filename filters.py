import math 
from PIL import Image
image = Image.open('earthimg.jpg')

def load_img(filename): 
    image = Image.open(filename)
    return image

def show_img(img): 
    img.show(image)

def save_img(img, filename):
    img.save(filename)

def obamicon(img): 
    n_data = []
    data = img.getdata()

    for pixel in data: 
        photo_intensity = pixel[0] + pixel[1] + pixel[2]

        if photo_intensity < 182: 
            n_data.append((0, 51, 76))
        elif photo_intensity >= 182 and photo_intensity < 364: 
            n_data.append((217, 26, 33))
        elif photo_intensity >= 364 and photo_intensity < 546: 
            n_data.append((112, 150, 158))
        elif photo_intensity >= 546: 
            n_data.append(( 252, 227, 166))

       # dark_blue = photo_intensity < 182
        #red = photo_intensity >= 182 and photo_intensity < 364
        #light_blue = photo_intensity >= 364 and photo_intensity < 546
       # yellow = photo_intensity > 546

    new_image = Image.new(img.mode, img.size)
    new_image.putdata(n_data)
    
    return new_image 






# def insert(base, color, source, destination)
   


   