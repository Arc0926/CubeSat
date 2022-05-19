import sys,os
import cv2
import numpy as np
from PIL import Image, ImageEnhance
import time
def plastic_detection(img_file_path):
    absolutepath = os.path.abspath(__file__)
    parentDirectory = os.path.dirname(os.path.dirname(absolutepath))
    fileName = os.path.join(parentDirectory, img_file_path).replace("\\","/")
    # Reading the image
    img = cv2.imread(fileName)

    # convert to hsv colorspace
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    saturation = hsv[:, :, 1].mean()
    print(saturation)
    # lower bound and upper bound for Blue

    lower_bound_b = np.array([100,60,70])  
    upper_bound_b = np.array([130,255,255])
    # find the colors within the boundaries
    mask = cv2.inRange(hsv, lower_bound_b, upper_bound_b)


    #mask = mask_g + mask_r + mask_b
    mask = cv2.bitwise_not(mask)



    mask_path = parentDirectory.replace("\\", "/") + '/Images/Masks/mask.jpg' % (t)
    cv2.imwrite(mask_path, mask)
    # Showing the output
    '''
    cv2.imshow("Image", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''

#plastic_detection('C:/Users/Arcan/Documents/CubeSat/Images/green.png', 3)
plastic_detection('Images/demo.jpg')