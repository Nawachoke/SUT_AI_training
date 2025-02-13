import cv2
import numpy as np

def display_image(x):
    pass

kid_image = cv2.imread("day8/data/captured_image.jpg")
kid_image = cv2.GaussianBlur(kid_image, (5, 5), 3)
kid_image = cv2.cvtColor(kid_image, cv2.COLOR_BGR2HSV)
cv2.namedWindow("HSV Adjustments", cv2.WINDOW_NORMAL)
cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
cv2.createTrackbar("H Min", "HSV Adjustments", 0, 179, display_image)
cv2.createTrackbar("H Max", "HSV Adjustments", 179, 179, display_image)
cv2.createTrackbar("S Min", "HSV Adjustments", 0, 255, display_image)
cv2.createTrackbar("S Max", "HSV Adjustments", 255, 255, display_image)
cv2.createTrackbar("V Min", "HSV Adjustments", 0, 255, display_image)
cv2.createTrackbar("V Max", "HSV Adjustments", 255, 255, display_image)

while True:
    h_min = cv2.getTrackbarPos("H Min", "HSV Adjustments")
    h_max = cv2.getTrackbarPos("H Max", "HSV Adjustments")
    s_min = cv2.getTrackbarPos("S Min", "HSV Adjustments")
    s_max = cv2.getTrackbarPos("S Max", "HSV Adjustments")
    v_min = cv2.getTrackbarPos("V Min", "HSV Adjustments")
    v_max = cv2.getTrackbarPos("V Max", "HSV Adjustments")

    lower_hsv = np.array([h_min, s_min, v_min])
    upper_hsv = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(kid_image, lower_hsv, upper_hsv)
    result = cv2.bitwise_and(kid_image, kid_image, mask=mask)

    cv2.imshow("Result", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()