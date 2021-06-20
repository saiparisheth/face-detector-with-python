import cv2
from random import randrange

#loading some pre-trained face data form opecv
trained_face_data = cv2.CascadeClassifier('face_data.xml')

#choosing an file for detecting faces
#img = cv2.imread('pam-beesly.jpg')
#live catch from webcam
web_cam = cv2.VideoCapture(0)
while True:

    #reading the current frame
    successful_frame_read, frame = web_cam.read()
    #converting the image to greyscale
    grayscale_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detecting face
    face_coordinates = trained_face_data.detectMultiScale(grayscale_img)
    #drawing a rectangle
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (randrange(128,256), randrange(128,256), randrange(128,256)), 2)
    cv2.imshow('the photo0', frame)
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break
web_cam.release()
"""
#detecting face
face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

#drawing a rectangle
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(128,256), randrange(128,256), randrange(128,256)), 2)
print(x,y,h,w)
#just displaying the image
cv2.imshow('the photo0', img)
cv2.waitKey()
"""