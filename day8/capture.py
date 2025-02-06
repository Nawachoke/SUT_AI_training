import cv2

# Open a connection to the webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Capture a single frame
ret, frame = cap.read()

if ret:
    # Save the captured image to a file
    cv2.imwrite('captured_image.jpg', frame)
    print("Image captured and saved as 'captured_image.jpg'")
else:
    print("Error: Could not capture image.")

# Release the webcam
cap.release()
# Close any OpenCV windows
cv2.destroyAllWindows()