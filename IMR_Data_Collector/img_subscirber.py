#!/usr/bin/env python
from __future__ import print_function

import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2
import os
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from PIL import Image as IMG
import numpy as np

new_folder_name = 1

'''
for folder_name in os.listdir('data'):
	print(int(folder_name))
	print(new_folder_name)
	if int(folder_name) > new_folder_name:
		new_folder_name = int(folder_name)
new_folder_name += 1
'''
new_folder_name = '%04d' % (new_folder_name, )
print(new_folder_name)

rgb_path = os.path.join('data', new_folder_name, 'rgb')
depth_path = os.path.join('data', new_folder_name, 'depth')
#os.makedirs(rgb_path)
#os.makedirs(depth_path)

img_idx = 0

class image_converter:

  def __init__(self):
    #self.image_pub = rospy.Publisher("image_topic_2",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/color/image_raw",Image,self.callback)
    self.depth_sub = rospy.Subscriber("/camera/depth/image_raw",Image,self.callback2)
    self.rgb_img = None
    self.depth_img = None

  def callback(self,data):
    global img_idx
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      self.rgb_img = cv_image
    except CvBridgeError as e:
      print(e)

    cv2.imshow("Image window", cv_image)

    key = cv2.waitKey(3)
    if key == ord('s'):
    	print("saving images")
    	self.save_imgs()
    	#print( os.path.join(rgb_path , '%04d.jpg' % (img_idx,)) )
    	#cv2.imwrite(os.path.join(rgb_path , '%04d.jpg' % (img_idx,)), cv_image)
    	img_idx+=1

  def callback2(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "passthrough")
      self.depth_img = cv_image
    except CvBridgeError as e:
      print(e)

    #cv2.imshow("depth window", cv_image)

  def save_imgs(self):
  	#cv2.imwrite(, self.rgb_img)
    # to store value greater than 255, you need to first convert your depth image array to 16 bit
    self.depth_img = self.depth_img*1000
    (unique, counts) = np.unique(self.depth_img, return_counts=True)
    frequencies = np.asarray((unique, counts)).T
    print(frequencies)
    print(self.depth_img)

    cv2.imwrite(os.path.join(depth_path , '%04d.png' % (img_idx,)), self.depth_img.astype(np.uint16))
    cv2.imwrite(os.path.join(rgb_path , '%04d.png' % (img_idx,)), self.rgb_img)
    print('rgb & depth image saved: ',  '%04d.png' % (img_idx,) )
 


def main(args):
  ic = image_converter()
  #dic = depth_image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)