import requests
import cv2
import numpy as np
import imutils
from PIL import Image
import os

# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.0.100:8080/shot.jpg"
face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
# While loop to continuously fetching data from the Url
# img = cv2.imread(url)
# print('img: ', img)

# cv2.imshow("Android_cam", img)
# while True:
#     img_resp = requests.get(url)
#     print('img_resp: ', img_resp)
#     img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
#     img = cv2.imdecode(img_arr, -1) 
#     # print('img: ', img)
#     img = imutils.resize(img, width=1000, height=1800)
#     cv2.imshow("Android_cam", img)
  
#     # Press Esc key to exit
#     if cv2.waitKey(1) == 27:
# #         break
  
# cv2.destroyAllWindows()

def xuat_cam(name):
    recognizer.read(f"./data/classifiers/{name}_classifier.xml")
    pred = 0
    img_resp = requests.get(url)
    img = np.array(bytearray(img_resp.content),dtype= np.uint8)
    img = cv2.imdecode(img,-1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h,x:x+w]
        id,confidence = recognizer.predict(roi_gray)
        confidence = 100 - int(confidence)
        if confidence > 50:
            pred = 1
            text = name
            font = cv2.FONT_HERSHEY_PLAIN
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            img = cv2.putText(img, text, (x, y-4), font, 1, (0, 255, 0), 1, cv2.LINE_AA)
        else:
            pred = -1
            text = "UnknownFace"
            font = cv2.FONT_HERSHEY_PLAIN
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            img = cv2.putText(img, text, (x, y-4), font, 1, (0, 0,255), 1, cv2.LINE_AA)

    img = imutils.resize(img,width=256,height=400)
    img = Image.fromarray(img)
    return img,pred

def nhan_dien_khuon_mat(name,num_of_images):
    path = "./data/" + name
    if not os.path.exists(path):
        os.makedirs(path)
    detector = cv2.CascadeClassifier("./data/haarcascade_frontalface_default.xml")
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    new_img = None
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = detector.detectMultiScale(image=grayimg, scaleFactor=1.1, minNeighbors=5)

    for x, y, w, h in face:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)
            cv2.putText(img, "Face Detected", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))
            cv2.putText(img, str(str(num_of_images)+" images captured"), (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))
            new_img = img[y:y+h, x:x+w]
    img = imutils.resize(img, width=250, height=100)
    img = Image.fromarray(img)
    try :
        cv2.imwrite(str(path+"/"+str(num_of_images)+name+".jpg"), new_img)
        num_of_images += 1
    except :
        pass
    return img,num_of_images