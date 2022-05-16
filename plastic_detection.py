import sys,os
import cv2
import numpy as np
def plastic_detection(img_file_path, tolerance):
    absolutepath = os.path.abspath(__file__)
    parentDirectory = os.path.dirname(absolutepath)
    print(parentDirectory)
    filename = os.path.join(parentDirectory, img_file_path).replace("\\","/")
    # Reading the image
    print(filename)
    img = cv2.imread(filename)

    # convert to hsv colorspace
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # lower bound and upper bound for Green color
    lower_bound = np.array([50, 20, 20])   
    upper_bound = np.array([100, 255, 255])
    # find the colors within the boundaries
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Showing the output
    cv2.imshow("Image", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#plastic_detection('C:/Users/Arcan/Documents/CubeSat/Images/green.png', 3)
plastic_detection('Images/green.png', 3)