#! ./env/bin/python3
import os
from os.path import abspath, dirname, join, exists

import cv2
import numpy as np
from numpy import ndarray as NumpyArray

from src import image_enhance

ROOT = abspath(dirname(__file__))
IMG_FORMATS = ['jpg', 'png', 'jpeg']
IMGS_PATH = join(ROOT, 'images')
ENHANCED_PATH = join(ROOT, 'enhanced')
SUFFIX = '_enhanced.'

def image_enhance_from(image_file:str):
    img: NumpyArray = cv2.imread(image_file)
    if(len(img.shape)>2):
        img = np.dot(img[...,:3], [0.299, 0.587, 0.114])
    rows, cols = img.shape
    aspect_ratio = rows / cols
    new_rows: int = 350
    new_cols: int = int(new_rows / aspect_ratio)
    img: NumpyArray = cv2.resize(img, (new_cols, new_rows))
    enhanced_img: NumpyArray = image_enhance(img)
    enhanced_img = ((1 - enhanced_img) * 255).astype(np.uint8)
    return enhanced_img

def main():
    image_names = os.listdir(IMGS_PATH)
    image_names = list(filter(lambda fname: fname.split('.')
                       [-1] in IMG_FORMATS, image_names))

    print(f'Found {len(image_names)} images in "images" folder')

    print('Processing images ...')
    images_processed = False
    for i, img_name in enumerate(image_names):
        enhanced_img_name = img_name.split('.')
        enhanced_img_name = enhanced_img_name[0] + SUFFIX + enhanced_img_name[-1]
        if exists(join(ENHANCED_PATH, enhanced_img_name)):
            print(f'{img_name} is already processed: ({i+1}/{len(image_names)})')
            continue  # if an image exists its enhanced, nothing is done
        images_processed = True
        print(f'Processing {img_name}: ({i+1}/{len(image_names)})')
        enhanced_img = image_enhance_from(join(IMGS_PATH, img_name))
        cv2.imwrite(join(ENHANCED_PATH, enhanced_img_name), enhanced_img)

    if images_processed:
        print('\tAll enhanced images saved in the "enhanced" folder.')
    else:
        print('\tNo image was processed, it probably already exists')
        print('\tits enhanced versions in the "enhanced" folder.')
    print('done.')


if __name__ == '__main__':
    main()
