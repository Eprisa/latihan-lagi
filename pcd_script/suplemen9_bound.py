import cv2
import numpy as np
from matplotlib import pyplot as plt

imggambar = cv2.imread('leave2.jpg',0)
kernel = np.ones((5,5), np.uint8)

th2=cv2.adaptiveThreshold(imggambar,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,6)
th2=~th2

# imgCanny = cv2.Canny(imggambar,10,150)
# closing = cv2.morphologyEx(imgCanny, cv2.MORPH_CLOSE, kernel)

imgmg=cv2.morphologyEx(th2,cv2.MORPH_GRADIENT,kernel)

tampil_hor=np.concatenate((imggambar,th2),axis=0)
# tampil_hor=np.concatenate((imggambar,mg),axis=0)

cv2.imshow('Boundary Extraction',tampil_hor)

cv2.waitKey(0)
cv2.destroyAllWindows
