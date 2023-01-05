import cv2
import numpy as np

# Define the lower and upper boundaries of the blue color
# in the HSV color space
blue_lower = np.array([100,50,50])
blue_upper = np.array([140,255,255])

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the frame from the webcam
    _, frame = cap.read()

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the blue color
    mask = cv2.inRange(hsv, blue_lower, blue_upper)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Iterate over the contours
    for contour in contours:
        # Check if the contour is a square
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        if len(approx) == 4:
            # Classify the square as "true"
            print("True")
        else:
            # Classify the square as "false"
            print("False")
    
    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
cap.release()
