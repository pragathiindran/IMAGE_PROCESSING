import cv2
import numpy as np

img=cv2.imread('abc.jpg')
#edge-detection
kernel=np.array([[-1,-1,-1],
                 [-1,8,-1],
                 [-1,-1,-1]])
#blurring
kernel1=np.array([[0.0625,0.125,0.0625],
                 [0.125,0.25,0.125],
                 [0.0625,0.125,0.0625]])

dst=cv2.filter2D(img,-1,kernel)
dst1=cv2.filter2D(img,-1,kernel1)
dst2=cv2.blur(img,(9,9))
cv2.imshow('Image input',img)
cv2.imshow('Image output(edge-detection)',dst)
cv2.imshow('Image output(blur)',dst1)
cv2.imshow('Image output',dst2)
cv2.waitKey()
cv2.destroyAllWindows()
