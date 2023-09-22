import cv2
import numpy as np
#import requests
from urllib import request

# Initialize variables
enter_count = 0
exit_count = 0

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize video capture
cap = cv2.VideoCapture(0)

# Define the x-axis line (adjust as needed)
x_axis = 300

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangle around faces and detect head position
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Check if head crosses the x-axis line
        if y + h < x_axis:
            enter_count += 1
            form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeyAmpyP_250tMANwurE0vYpttyE4NL60zBNOoM4qTcFbz0Og/formResponse?usp=pp_url&entry.155842951={}&submit=Submit".format(enter_count)
            request.urlopen(form_url)
        else:
            exit_count += 1
            # form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeyAmpyP_250tMANwurE0vYpttyE4NL60zBNOoM4qTcFbz0Og/formResponse?usp=pp_url&entry.724700286={}&submit=Submit".format(exit_count)
            # request.urlopen(form_url)

    # Display the frame with annotations
    cv2.line(frame, (0, x_axis), (frame.shape[1], x_axis), (0, 255, 0), 2)
    cv2.putText(frame, f'Enter: {enter_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, f'Exit: {exit_count}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Crowd Detector', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
