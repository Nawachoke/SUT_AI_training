import cv2
import numpy as np

# video = cv2.VideoCapture('day8/data/street.mp4')
video = cv2.VideoCapture(0)
masker = {'Yellow':   np.array([[11, 61, 179], [85, 151, 255]]),
          'Black': np.array([[19, 45, 29], [170, 127, 147]]), 
          'Blue':  np.array([[30, 139, 0], [180, 255, 180]])}

mask_name = list(masker.keys())
color_counter = {'Yellow': 0, 'Black': 0, 'Blue': 0}
threshold = 500

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
                    if mask_name[i] == 'Yellow':
                        color = (0, 255, 255)
                        color_counter['Yellow'] += 1
                    elif mask_name[i] == 'Black':
                        color = (0, 0, 0)
                        color_counter['Black'] += 1
                    else:
                        color = (255, 0, 0)
                        color_counter['Blue'] += 1
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                    cv2.putText(frame, mask_name[i], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        counter_text = f"Yellow: {color_counter['Yellow']} Black: {color_counter['Black']} Blue: {color_counter['Blue']}"
        cv2.putText(frame, counter_text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        color_counter = {'Yellow': 0, 'Black': 0, 'Blue': 0}
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
video.release()
cv2.destroyAllWindows()