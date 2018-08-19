import cv2,os
import numpy as np
from PIL import Image 
import pickle
import hackathon as hck
ceye="cascades/haarcascade_eye.xml"
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('tra.yml')
cascadePath = "cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'faceR/face/'
import sqlite3
pop=0
conn=sqlite3.connect('table.db')
c=conn.cursor()

def read_db(idd):
    c=conn.cursor()
    c.execute('SELECT NAME FROM TBLEE WHERE ID=?', [idd])
    data=c.fetchall()
    print(data)
    

def start():
    nbr_predicted=0
    conf=0
    c=0
    font = cv2.FONT_HERSHEY_SIMPLEX
    cam = cv2.VideoCapture(0)
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        for(x,y,w,h) in faces:
            conf=0
            nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
            cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
            read_db(nbr_predicted)
            if not  (nbr_predicted==c):
                    hck.set(nbr_predicted,5)
                    c=nbr_predicted

            cv2.putText(im,str(nbr_predicted)+"--"+str(conf), (x, 50),font, 1.0, (255, 255, 0), lineType=cv2.LINE_AA)
            cv2.imshow('im',im)
            #print(nbr_predicted)
        if cv2.waitKey(1)==ord('q') :
            cam.release()
            break 





