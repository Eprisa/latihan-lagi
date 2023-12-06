import cv2
import numpy as np
from matplotlib import pyplot as plt

imggambar = cv2.imread("man.jpeg",-1)

# ===========
cv2.imshow("citra original",imggambar)
imgCropped = imggambar[00:300,0:350]
cv2.imshow("citra hasil crop",imgCropped)
# cv2.imshow("citra hasil crop",imggambar)
cv2.waitKey(0)
cv2.destroyAllWindows