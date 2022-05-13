import cv2
import numpy as np
def plastic_detection(img_file_path, threshold):
    # Reading the image
    img = cv2.imread(img_file_path)
    # Showing the output
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

plastic_detection('C:/Users/Arcan/Documents/CubeSat/Images/doggy.jpg', 3)