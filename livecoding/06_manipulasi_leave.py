import cv2
import numpy as np

imggambar = cv2.imread('leave.jpg', 0)

# Create a black background image
black_background = np.zeros_like(imggambar)

# Stack the original image and equalized image on the black background
hasil = np.hstack((imggambar, black_background))
imgresize = cv2.resize(hasil, (650, 400))
cv2.imshow('Hasil Equalisasi Histogram', imgresize)

cv2.waitKey(0)
cv2.destroyAllWindows()