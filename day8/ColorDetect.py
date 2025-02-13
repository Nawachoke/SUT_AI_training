import cv2
import numpy as np

img = cv2.imread('day8/data/colorballs.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

masker = {'Red': np.array([[0, 50, 50], [10, 255, 255], [0, 0, 255]]),
          'Green': np.array([[40, 20, 50], [90, 255, 255], [0, 255, 0]]),
          'Blue': np.array([[100, 50, 50], [180, 255, 255], [255, 0, 0]])}

class colorModel:
    def __init__(self, name, lower, upper, color):
        self.name = name
        self.lower = lower
        self.upper = upper
        self.color = color

mask_list = [colorModel(name, lower, upper, color) for name, (lower, upper, color) in masker.items()]

for i in range(len(masker)):
    # mask = cv2.inRange(hsv, masker[mask_name[i]][0], masker[mask_name[i]][1])
    mask = cv2.inRange(hsv, mask_list[i].lower, mask_list[i].upper)
    contours, hier = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            if mask_list[i].name == 'Red':
                color = (0, 0, 255)
            elif mask_list[i].name == 'Green':
                color = (0, 255, 0)
            else:
                color = (255, 0, 0)
            x, y, w, h = cv2.boundingRect(contour)
            print(x, y, w, h)
            # cv2.rectangle(img, (x, y), (x+w, y+h), mask_list[i].color, 2)
            # cv2.putText(img, mask_list[i].name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, mask_list[i].color, 2)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()