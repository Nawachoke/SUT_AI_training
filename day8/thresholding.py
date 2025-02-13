import cv2
import matplotlib.pyplot as plt

gray = cv2.imread('day8/data/kid.jpg', 0)
thresh, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
thresh, th2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
thresh, th3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
thresh, th4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
thresh, th5 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)
thresh, th6 = cv2.threshold(gray, 127, 255, cv2.THRESH_MASK)
thresh, th7 = cv2.threshold(gray, 127, 255, cv2.THRESH_OTSU)


images = [gray, th1, th2, th3, th4, th5, th6, th7]
titles = ['Original', 'Binary', 'Binary Inv', 'Trunc', 'Tozero', 'Tozero Inv', 'Mask', 'Otsu']

plt.figure(figsize=(10, 5))
for i in range(len(images)):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()