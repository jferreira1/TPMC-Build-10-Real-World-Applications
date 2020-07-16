import cv2
import os

pathname = r"C:\Users\Ferreira\Desktop\The Python Mega Course\Exercises\Section 25\facedetection\images"
face_cascade = cv2.CascadeClassifier(r"Exercises\Section 25\facedetection\haarcascade_frontalface_default.xml")

files = os.scandir(pathname)
for file in files:

    img = cv2.imread(os.path.join(pathname, file))
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img, 
    scaleFactor=1.05,
    minNeighbors=3)

    print(faces)
    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    if not ("_detected.jpg" in file.name) and (faces != ()):
        fullpath = os.path.join(pathname, file.name)
        filename = os.path.splitext(fullpath)[0] + "_detected.jpg"
        cv2.imwrite(filename, img)
