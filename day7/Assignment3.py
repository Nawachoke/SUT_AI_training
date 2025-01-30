import cv2
import numpy as np

video = cv2.VideoCapture('day7/data/street.mp4')
masker = {'Red': np.array([[0, 50, 50], [10, 255, 255]]),
          'Green': np.array([[40, 20, 50], [90, 255, 255]]), 
          'Blue': np.array([[100, 50, 50], [180, 255, 255]])}

mask_name = list(masker.keys())
color_counter = {'Red': 0, 'Green': 0, 'Blue': 0}
threshold = 1000

while (video.isOpened()):
    ret, frame = video.read()
    if ret:
        frame = cv2.resize(frame, (640, 480))
        frame2mask = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        for i in range(len(masker)):
            mask = cv2.inRange(frame2mask, masker[mask_name[i]][0], masker[mask_name[i]][1])
            contours, hier = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            for contour in contours:
                area = cv2.contourArea(contour) > 1000
                if area:
                    if mask_name[i] == 'Red':
                        color = (0, 0, 255)
                        color_counter['Red'] = len(contours[area])
                    elif mask_name[i] == 'Green':
                        color = (0, 255, 0)
                        color_counter['Green'] = len(contours)
                    else:
                        color = (255, 0, 0)
                        color_counter['Blue'] = len(contours)
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                    cv2.putText(frame, mask_name[i], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        counter_text = f"Red: {color_counter['Red']} Green: {color_counter['Green']} Blue: {color_counter['Blue']}"
        cv2.putText(frame, counter_text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
video.release()
cv2.destroyAllWindows()