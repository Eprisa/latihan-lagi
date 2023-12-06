import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
imggambar = cv2.imread("lampu.png", 0)
thresh = 170
img_binary = cv2.threshold(imggambar, thresh, 255, cv2.THRESH_BINARY)[1]
(cnt, hierarchy) = cv2.findContours(
    (img_binary), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("JUMLAH OBJEK PADA CITRA : ", len(cnt))
cv2.imshow('output', img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()