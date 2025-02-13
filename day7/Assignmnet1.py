import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        # strXY = str(x) + ', ' + str(y)
        color = img[y, x]
        strXY = f'({color[0]}, {color[1]}, {color[2]})'
        cv2.putText(img, strXY, (x, y), font, 1, (100, 100, 100), 2)
        cv2.imshow('image', img)

img = cv2.imread('day7/data/RGB.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()