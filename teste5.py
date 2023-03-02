import cv2

capture = cv2.VideoCapture(0)
faceClassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeClassifier = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detecta = faceClassifier.detectMultiScale(gray)
    for (x, y, w, h) in detecta:
        retanguloFace = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        localOlho = retanguloFace[y:y + h, x:x + w]
        localOlhoCinza = cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY)
        detectado = olho.detectMultiScale(localOlhoCinza, 1.3, 9)

        for (ox, oy, ol, oa) in detectado:
            cv2.rectangle(localOlho, (ox, oy), (ox + ol, oy + oa), (255, 0, 0), 2)

    # Redimensionando
    # redimensionado = cv2.resize(frame, (455, 350))
    # Exibindo na tela
    cv2.imshow('frame', frame)

    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break
capture.release()

# while not cv2.waitKey(20) & 0xFF == ord('q'):
#     ret, frame = capture.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = faceClassifier.detectMultiScale(gray)
#     for x, y, w, h in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     cv2.imshow('frame', frame)
#     cv2.imshow('gray', gray)

