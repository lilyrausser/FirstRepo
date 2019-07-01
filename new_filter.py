import math 
from PIL import Image 


def load_image(filename): 
    image = Image.open(filename)
    return image

def show_image(img): 
    img.show()

def save_image(img,filename): 
    img.save(filename)
    


def penguie(img): 
    n_data = []
    data = img.getdata()

    for pixel in data: 
        photo_intensity = pixel[0] + pixel[1] + pixel[2]
        if photo_intensity <= 185:
            n_data.append((0, 100, 0))
        elif photo_intensity >= 185 and photo_intensity < 356:
            n_data.append((0, 150, 50))
        elif photo_intensity >= 356 and photo_intensity < 546:
            n_data.append((267, 350, 500))
        elif photo_intensity >= 546:
            n_data.append((365, 247, 1200))
    new_image = Image.new(img.mode, img.size)
    new_image.putdata(n_data)

    return new_image 

def penguin_2(img): 
    n_data = []
    data = img.getdata()

    for pixel in data: 
        photo_intensity = pixel[0] + pixel[1] + pixel[2]

        if photo_intensity <= 100:
            n_data.append((0, 100, 0))
        elif photo_intensity >= 100 and photo_intensity < 200:
            n_data.append((10, 110, 10))
        elif photo_intensity >= 200 and photo_intensity < 300:
            n_data.append((20, 120, 20))
        elif photo_intensity >= 300 and photo_intensity < 400:
            n_data.append((30, 130, 30 ))
        elif photo_intensity >= 400 and photo_intensity < 500:
            n_data.append((40, 140, 40))
        elif photo_intensity >= 500 and photo_intensity < 600:
            n_data.append((50, 150, 50))
        elif photo_intensity >= 600 and photo_intensity < 700:
            n_data.append((60, 160, 60))
        elif photo_intensity >= 700 and photo_intensity < 800:
            n_data.append((70, 170, 70))
        elif photo_intensity >= 800 and photo_intensity < 900:
            n_data.append((80, 180, 80))
        elif photo_intensity >= 900 and photo_intensity <1000: 
            n_data.append((90, 190, 90))
        elif photo_intensity > 1000:
            n_data.append((100, 200, 100))

    new_image = Image.new(img.mode, img.size)
    new_image.putdata(n_data)

    return new_image 