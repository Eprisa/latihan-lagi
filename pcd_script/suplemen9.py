import cv2
import numpy as np
imggambar = cv2.imread('a_noise_dua.jpg',0)

kernel = np.ones((15,15),np.uint8)

(thresh, im_bw) = cv2.threshold(imggambar, 200, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

operasi = cv2.threshold(imggambar, 200, 255, cv2.THRESH_BINARY)

operasi = cv2.erode(imggambar,kernel,iterations = 1)

operasi = cv2.dilate(imggambar,kernel,iterations = 1)

tampil_hor=np.concatenate((im_bw,operasi),axis=1)
cv2.imshow('hasil',tampil_hor)
cv2.waitKey(0)
cv2.destroyAllWindows