import cv2
import sys
import numpy as np

video_capture = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()


    kernel1 = np.ones((5,5),np.float32)/150
    kernel2 = np.ones((5,5),np.uint8)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #dst = cv2.filter2D(frame,-1,kernel1)
    #blur = cv2.blur(frame,(30,30))
    #gradient = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel2)
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    #sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
    #sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),

    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', laplacian)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
