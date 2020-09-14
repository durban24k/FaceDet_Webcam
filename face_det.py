import cv2

filePath = 'videofile.xml'
faceCascade = cv2.CascadeClassifier(filePath)
capture = cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.1,5)
    for (x, y, w, h) in faces: # Draw a rectangle around the faces
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Video', frame) # Display the resulting frame
    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        break

capture.release() # When everything is done, release the capture
cv2.destroyAllWindows