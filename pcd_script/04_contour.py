import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

imggambar = cv2.imread("gambar1b.png", 0)

kernel2 = np.ones((15, 15), np.uint8)
thresh = 170

cv2.putText(imggambar,"14",(0,20),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
imgbinary = cv2.threshold(imggambar,thresh, 255, cv2.THRESH_BINARY)[1]
imginvers = ~imgbinary
imgdilation = cv2.dilate(imggambar, kernel2, iterations=1)
tampil_hor = np.concatenate((imgbinary, imginvers), axis=1)

cv2.imshow('hasil contour', imginvers)
cv2.waitKey(0)
cv2.destroyAllWindows()