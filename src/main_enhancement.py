# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pylab as plt;
import scipy.ndimage
import sys
import imageio
import matplotlib

from image_enhance import image_enhance

if(len(sys.argv)<2):
    print('loading sample image');
    img_name = '1.jpg'
    img = scipy.ndimage.imread('../images/' + img_name);
elif(len(sys.argv) >= 2):
    img_name = sys.argv[1];
    img = scipy.ndimage.imread(sys.argv[1]);
    
if(len(img.shape)>2):
    img = np.dot(img[...,:3], [0.299, 0.587, 0.114]);

rows,cols = np.shape(img);
aspect_ratio = np.double(rows)/np.double(cols);

new_rows = 350;             #randomly selected number
new_cols = new_rows/aspect_ratio;

img = scipy.misc.imresize(img,(np.int(new_rows),np.int(new_cols)));

enhanced_img = image_enhance(img);    

if(1):
    print('saving the image')
    matplotlib.image.imsave('../enhanced/' + 'enhanced.jpg', enhanced_img)
else:
    plt.imshow(enhanced_img,cmap = 'Greys_r');
