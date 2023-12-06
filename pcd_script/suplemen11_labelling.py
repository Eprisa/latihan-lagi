import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.zeros((300,300,3),np.uint8)
img[100:150,200:240]=255,0,0
cv2.line(img,(0,0),(150,150),(0,0,100),3)
cv2.rectangle(img,(120,140),(50,180),(0,200,0),2)
cv2.circle(img,(100,100),70,(255,0,255),6)
cv2.putText(img,"Identifikasi Objek",(100,175),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255),1)

cv2.imshow("bghitam",img)

cv2.waitKey(0)
cv2.destroyAllWindows