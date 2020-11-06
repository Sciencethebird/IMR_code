import numpy as np
import cv2
import os
from PIL import Image
import sys
import argparse
import matplotlib.pyplot as plt

rgb_path = os.path.join('data', '0001', 'rgb')
image_path = os.path.join(rgb_path, '0000.png')
img = np.array(Image.open(image_path))

output_folder = 'mask_test'

print("**** value count ****")
(unique, counts) = np.unique(img, return_counts=True)
print(unique)

print(img[250, 300, :])

#plt.imshow(img)
#plt.show()



item_color = np.array([102, 102, 255])
item_color_2 = np.array([102, 102, 122])
item_mask = img
for i in range(img.shape[0]):
	for j in range(img.shape[1]):

		if  np.array_equal(img[i, j, :], item_color):
			item_mask[i, j] = [255, 255, 255]
		else:
			item_mask[i, j] = [0, 0, 0]
		#print(img[i, j, 0])
		#pass
		#print(img[i, j, :])


print(item_mask)
(unique, counts) = np.unique(img, return_counts=True)
frequencies = np.asarray((unique, counts)).T
print(frequencies)
plt.imshow(item_mask)
plt.show()

# https://stackoverflow.com/questions/38198379/how-to-change-the-pixel-values-of-an-image
'''
img = Image.new( im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if 205 in pixelMap[i,j]:
            pixelMap[i,j] = (0,0,0,255)
        else:
            pixelsNew[i,j] = pixelMap[i,j]

'''