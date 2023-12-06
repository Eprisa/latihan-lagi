import cv2
import numpy as np
from matplotlib import pyplot as plt

imggambar = cv2.imread('patung.jpeg',-1)

kernel = np.ones((15,15), np.uint8)

imgCanny = cv2.Canny(imggambar,10,150)
imgclosing = cv2.morphologyEx(imggambar, cv2.MORPH_CLOSE, kernel)

imgmg=cv2.morphologyEx(imggambar,cv2.MORPH_GRADIENT,kernel)
cv2.putText(imggambar,"Eprisa Nova rahmawati",(70,175),cv2.FONT_HERSHEY_COMPLEX,0.5,(62, 254, 255),1)

tampil_hor=np.concatenate((imggambar,imgclosing),axis=0)
# tampil_hor=np.concatenate((imggambar,mg),axis=0)

cv2.imshow('Closing',tampil_hor)

cv2.waitKey(0)
cv2.destroyAllWindows
