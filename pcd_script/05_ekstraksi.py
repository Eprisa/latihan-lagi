import cv2
import numpy as np
from matplotlib import pyplot as plt
imggambar = cv2.imread('gambar2b.jpg', 0)
kernel = np.ones((20, 20), np.uint8)
kernel2 = np.ones((10, 10), np.uint8)
imgCanny = cv2.Canny(imggambar, 10, 150)
tampil_hor = np.concatenate((imggambar, imgCanny), axis=0)
imgresize = cv2.resize(tampil_hor, (400, 450))
cv2.imshow('Hasil ekstraksi', imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()