import cv2
detector=cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
offset=50
import sqlite3

def create_db(uid,name):
    conn=sqlite3.connect('table.db')
    c=conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS TBLEE(ID INT,NAME VARCHAR(20))')
    c.execute('INSERT INTO TBLEE VALUES(?,?)',(uid,name))
    conn.commit()
    conn.close()
    
def data(uid,name):
    
    cam = cv2.VideoCapture(0)
    i=0
    create_db(uid,name)
    while True:
        if i==50:
            break    
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        for(x,y,w,h) in faces:
            i=i+1
            print('a')
            cv2.imwrite("faceR/face/"+'face'+uid+'.'+ str(i) +'.'+ ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
            cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
            cv2.imshow('im',im[y:y+h,x:x+w])
            cv2.waitKey(10)
            if i==50:
                cam.release()
                cv2.destroyAllWindows()
                break
            break
        




