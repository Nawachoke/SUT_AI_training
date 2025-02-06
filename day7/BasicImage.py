import cv2
import numpy as np 
img = cv2.imread('day7/data/cat.jpg')
cv2.imshow('cat', img)
cv2.waitKey(0)
cv2.destroyAllWindows()