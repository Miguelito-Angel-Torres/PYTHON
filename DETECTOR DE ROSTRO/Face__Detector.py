import cv2 #Importacion de la Libreria
from random import randrange
#https://github.com/opencv/opencv/tree/master/data/haarcascades (Importante)
#https://docs.opencv.org/2.4/index.html
#https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html?highlight=.cvtcolor#cv2.cvtColor
#Importacion 
#https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html?highlight=detectmultiscale
#trained_face_data = cv2.CascadeClassifier('../ha.xml')

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

#Choose an image to dectect face in
#IMPORTACION DE IMAGEN EN OPENCV

img = cv2.imread("FVQR3HBX3JEXTGFT27UCAF7FQU.jpg")
#img = cv2.imread("jose-antonio-primo-de-rivera-c480gc.jpg")

#Must convert to grayscale
# Convercion la imagen en el color gises
# img a quien , color_bgr2gray q tipo 
grayscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#Detectacion de rostro
# Detect faces

#detectMuiltiScales = "Duelve las coordinadas de los rectangulos"

face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
#print(face_coordinates)


#Draw rectangles around the faces
#creacion de rectangulo en el rostro
#(x,y,w,h) = face_coordinates[0]

for(x,y,w,h) in face_coordinates:
    cv2.rectangle(img,(x ,y),(x+w, y+h),(randrange(128,256), randrange(128,256),randrange(128,256)),10)


#cv2.rectangle(img,(247 ,45),(247+367, 45+367),(0,255,0),2)


#for(x,y,w,h) in face_coordinates:
    #cv2.rectangle(img,(247 ,45),(247+367, 45+367),(0,255,0),2)
    




# Con este metod se abre y se cierra aplastando un boton 

cv2.imshow('Miguel Programmer Face Detector' ,  img)
key = cv2.waitKey()



if key == 81 or key ==113:
    quit()
   


#key_press = cv2.waitKey(1)
#if key_press == 2: #The ascii code for spacebar
   # quit()#quits the programme when spacebar is hit