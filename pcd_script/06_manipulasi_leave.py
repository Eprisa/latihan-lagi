import cv2
import numpy as np
from matplotlib import pyplot as plt

imggambar = cv2.imread('leave.jpg',0)

kernel = np.ones((2,2), np.uint8)

imgCanny = cv2.Canny(imggambar,10,150)
imgclosing = cv2.morphologyEx(imggambar, cv2.MORPH_CLOSE, kernel)

imgmg = cv2.morphologyEx(imggambar, cv2.MORPH_GRADIENT, kernel,)
rows, cols = imgmg.shape[:2]
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
imgrotasi = cv2.warpAffine(imgmg, M, (cols, rows))

tampil_ver=np.concatenate((imggambar,imgclosing),axis=0)
tampil_ver=np.concatenate((imgclosing, imgrotasi),axis=1)

imgresize = cv2.resize(tampil_ver, (650, 400))
cv2.imshow('hasil',imgresize)

cv2.waitKey(0)
cv2.destroyAllWindows()