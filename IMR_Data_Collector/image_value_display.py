import numpy as np
import cv2
import os
from PIL import Image
import sys
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='specify file path')
parser.add_argument('file_path', help='specify your image path')
args = parser.parse_args()
print("input file: ", args.file_path)
print(os.getcwd())


#image_path = 'data/0001/depth/0001.png'
image_path = args.file_path
#img = cv2.imread(image_path)
img = np.array(Image.open(image_path))
print(img)

print("value count")
(unique, counts) = np.unique(img, return_counts=True)
frequencies = np.asarray((unique, counts)).T
print(frequencies)


plt.imshow(img)
plt.show()
#key = cv2.waitKey(300000)
 
#cv2.destroyAllWindows()