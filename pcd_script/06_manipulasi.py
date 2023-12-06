import cv2
import numpy as np
from matplotlib import pyplot as plt

imggambar = cv2.imread('leave.jpg',0)

kernel = np.ones((5,5), np.uint8)

rows, cols = imggambar.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
imgrotasi = cv2.warpAffine(imggambar, M, (cols, rows))

imgCanny = cv2.Canny(imggambar,10,150)
imgclosing = cv2.morphologyEx(imggambar, cv2.MORPH_CLOSE, kernel)
imgErode = cv2.erode(imgrotasi, kernel, iterations=1)

tampil_hor=np.concatenate((imggambar,imgclosing),axis=0)
tampil_hor = np.concatenate((imggambar, imgErode), axis=1)

imgresize = cv2.resize(tampil_hor, (650, 400))
cv2.imshow('Closing',imgresize)

cv2.waitKey(0)
cv2.destroyAllWindows()