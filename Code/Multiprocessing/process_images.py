import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    'img1.jpg',
    'img2.jpg',
    'img3.jpg',
    'img4.jpg',
    'img5.jpg',
    'img6.jpg',
    'img7.jpg',
    'img8.jpg',
    'img9.jpg',
    'img10.jpg'
]

t1 = time.perf_counter()
size = (1200, 1200)

def processImage(img_name):
    img = Image.open(f'Photos/{img_name}')
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'Processed/{img_name}')
    print(f'{img_name} was processed..')

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(processImage, img_names)

    t2 = time.perf_counter()
    print(f'finished in {t2 - t1} seconds')
    