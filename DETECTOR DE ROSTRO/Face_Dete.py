import cv2
from random import randrange
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

#img = cv2.imread('FVQR3HBX3JEXTGFT27UCAF7FQU.jpg')
# 0 es para poner la camara web # tambien archivo de un video mp4
#webcam = cv2.VideoCapture("sds.mp4")
webcam = cv2.VideoCapture(0)

#Iterate forever over frames
while True:
    #Read the current frames
    #primero es para verificar 
    successful_frame_read,frame = webcam.read()

    #Must convert to grayscale


    vidGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Detect faces
    faces = trained_face_data.detectMultiScale(vidGray)

    #Draw rectamgles around the faces

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x ,y),(x+w, y+h),(randrange(128,256), randrange(128,256),randrange(128,256)),10)


    cv2.imshow("Miguel Programmer" , frame)
    # solo va pasar un milisegundo
    key = cv2.waitKey(1)


    #Stop if Q key is pressed
    # 81,113 SIGNIFICA Q y q
    # https://elcodigoascii.com.ar/codigos-ascii/letra-q-mayuscula-codigo-ascii-81.html

    if key == 81 or key==113:
        break
#Limpiar
webcam.release()

"""faces = trained_face_data.detectMultiScale(imgGray)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 2) 
cv2.imshow("Face detector", img)
key = cv2.waitKey(1)
#key_press = cv2.waitKey(1)
#if key_press == 32: #The ascii code for spacebar
    #quit()#quits the programme when spacebar is hit


print("Lucas")"""

"""https://www.youtube.com/watch?v=XIrOM9oP3pA&t=8820s"""