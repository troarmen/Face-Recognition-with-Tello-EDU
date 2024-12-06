import cv2

xml_haar_cascade = r'../haarcascade_frontalface_alt2.xml'
xml_haar_eye = r'../haarcascade_eye.xml'

# Carregar Classificador
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)
eyeClassifier = cv2.CascadeClassifier(xml_haar_eye)

# Iniciar câmera
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceClassifier.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        olhoLocal = frame[y:y + h, x:x + w]
        olhoLocalCinza = cv2.cvtColor(olhoLocal, cv2.COLOR_BGR2GRAY)
        detectado = eyeClassifier.detectMultiScale(olhoLocalCinza)
        for(ox, oy, ol, oa) in detectado:
            cv2.rectangle(olhoLocal, (ox, oy),(ox + ol, oy + oa), (255, 0, 0), 2)

    # Exibindo na tela
    cv2.imshow('frame', frame)
    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()
