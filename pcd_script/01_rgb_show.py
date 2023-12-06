import cv2
import numpy as np
from matplotlib import pyplot as plt

imggambar = cv2.imread("gambar1b.png", 1)
tampil_hor = np.concatenate((imggambar, imggambar), axis=1)
cv2.putText(imggambar,"NIM_2103040144/Eprisa Nova Rahmawati",(5,15),cv2.FONT_HERSHEY_COMPLEX,0.5,(0, 0, 0),1)
tampil_hor = cv2.circle(imggambar, (470, 480), 15, (0), 5)


cv2.imshow("hasil", imggambar)
cv2.waitKey(0)
cv2.destroyAllWindows()
