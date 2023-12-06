import cv2
import numpy as np
from matplotlib import pyplot as plt

imggambar = cv2.imread("lampu.jpeg", 1)
tampil_hor = np.concatenate((imggambar, imggambar), axis=1)
cv2.putText(imggambar,"Eprisa Nova rahmawati",(5,15),cv2.FONT_HERSHEY_COMPLEX,0.5,(0, 0, 0),1)
cv2.putText(imggambar,"2103040144",(5,40),cv2.FONT_HERSHEY_COMPLEX,0.5,(0, 0, 0),1)
tampil_hor = cv2.rectangle(imggambar, (425, 425), (475, 475), (0), 5)
#tampil_hor = cv2.circle(imggambar, (450, 450), 25, (0), 5)


cv2.imshow("hasil", imggambar)
cv2.waitKey(0)
cv2.destroyAllWindows()
