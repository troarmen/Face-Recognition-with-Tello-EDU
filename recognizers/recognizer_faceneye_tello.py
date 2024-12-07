from functions import *
import cv2

xml_haar_cascade = r'../haarcascadeshaarcascade_frontalface_alt2.xml'
xml_haar_eye = r'../haarcascadeshaarcascade_eye.xml'

# Carregar Classificador
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)
eyeClassifier = cv2.CascadeClassifier(xml_haar_eye)
drone = initializeTello()
while True:
    img = telloGetFrame(drone, (320, 240))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceClassifier.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
        olhoLocal = img[y:y + h, x:x + w]
        olhoLocalCinza = cv2.cvtColor(olhoLocal, cv2.COLOR_BGR2GRAY)
        detectado = eyeClassifier.detectMultiScale(olhoLocalCinza)
        for (ox, oy, ol, oa) in detectado:
            cv2.rectangle(olhoLocal, (ox, oy), (ox + ol, oy + oa), (255, 0, 0), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
