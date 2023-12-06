import cv2
import numpy as np
from matplotlib import pyplot as plt

imggambar = cv2.imread("gambar1b.png",0)
kernel = np.ones((80,80),np.uint8)
kernel2 = np.ones((20, 20),np.uint8)

imgCanny = cv2.Canny(imggambar,10,150)
imgdilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgdilation2 = cv2.dilate(imgCanny,kernel2,iterations=1)
imgdilation3= ~imgdilation2

tampil_hor=np.concatenate((imggambar,imgdilation),axis=1)
tampil_hor=np.concatenate((imggambar,imgdilation2),axis=1)
tampil_hor=np.concatenate((imggambar,imgdilation3),axis=1)

# cv2.imshow('hasil akhir',tampil_hor)

cv2.imshow("hasil proses dilasi",imgdilation2)
cv2.waitKey(0)
cv2.destroyAllWindows