import cv2
import numpy as np

img=cv2.imread('pic.jpg')
windowName='Final Output'
cv2.namedWindow(windowName)

state_leftbtn=False

def blur_project(event,x,y,flags,param):
    global state_leftbtn
    if event==cv2.EVENT_LBUTTONDOWN:
        #cv2.line(img,(x,y),(x+50,y+50),(255,0,255),5)#BGR value
        state_leftbtn=True
        part=img[y:y+20,x:+20]
        blur=cv2.blur(part,(5,5))
        img[y:y+20,x:x+20]=blur
        #cv2.circle(img,(x,y),30,(0,0,255),2)

    elif event==cv2.EVENT_MOUSEMOVE:
        if state_leftbtn==True:
             part=img[y:y+20,x:x+20]
             blur=cv2.blur(part,(5,5))
             img[y:y+20,x:x+20]=blur
            #cv2.line(img,(x,y),(x+50,y+50),(255,0,255),5)#BGR value
            #cv2.circle(img,(x,y),30,(0,0,255),2)
            
    else:
        state_leftbtn=False
    
cv2.setMouseCallback(windowName,blur_project)
while True:
    cv2.imshow(windowName,img)
    if cv2.waitKey(1)==ord('q'):
        break;
cv2.destroyAllWindows()
