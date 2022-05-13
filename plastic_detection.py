import sys,os
import cv2
import numpy as np
def plastic_detection(img_file_path, tolerance):
    dir = os.path.dirname(img_file_path)
    filename = os.path.join(dir, img_file_path)
    # Reading the image
    img = cv2.imread(img_file_path)

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

plastic_detection('Images/green.png', 3)