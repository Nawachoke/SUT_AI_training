import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('day7/data/haarcascade_frontalface_default.xml')
scale_factor = 1.5
min_neighbors = 5
face_count = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    flip_frame = cv2.flip(frame, 1)
    face_coords = face_detector.detectMultiScale(flip_frame, scale_factor, min_neighbors)
    cv2.putText(flip_frame, f"Face Count: {len(face_coords)}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    for (x, y, w, h) in face_coords:
        cv2.rectangle(flip_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('frame', flip_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()