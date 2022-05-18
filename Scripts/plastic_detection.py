import sys,os
import cv2
import numpy as np
def plastic_detection(img_file_path, tolerance):
    absolutepath = os.path.abspath(__file__)
    parentDirectory = os.path.dirname(os.path.dirname(absolutepath))
    fileName = os.path.join(parentDirectory, img_file_path).replace("\\","/")
    # Reading the image
    img = cv2.imread(fileName)

    # convert to hsv colorspace
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # lower bound and upper bound for Green, Blue, and Red color
    lower_bound_g = np.array([50, 20, 20])   
    upper_bound_g = np.array([100, 255, 255])

    lower_bound_r1 = np.array([0, 50, 50]) 
    upper_bound_r1 = np.array([10, 255, 255]) 

    lower_bound_r2 = np.array([170, 50, 50]) 
    upper_bound_r2 = np.array([180, 255, 255]) 

    lower_bound_b = np.array([100,50,30])  
    upper_bound_b = np.array([130,255,255])
    # find the colors within the boundaries
    mask_g = cv2.inRange(hsv, lower_bound_g, upper_bound_g)
    mask_r1 = cv2.inRange(hsv, lower_bound_r1, upper_bound_r1)
    mask_r2 = cv2.inRange(hsv, lower_bound_r2, upper_bound_r2)
    mask_r = mask_r1 + mask_r2
    mask_b = cv2.inRange(hsv, lower_bound_b, upper_bound_b)


    mask = mask_g + mask_r + mask_b

    # Showing the output
    cv2.imshow("Image", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#plastic_detection('C:/Users/Arcan/Documents/CubeSat/Images/green.png', 3)
plastic_detection('Images/green.png', 3)