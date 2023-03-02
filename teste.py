import cv2


xml_haar_cascade = "haarcascade_frontalface_alt2.xml"

# Carregar Classificador
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)

# Iniciar câmera
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceClassifier.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    # Redimensionando
    redimensionado = cv2.resize(frame, (455, 350))
    # Exibindo na tela
    cv2.imshow('frame', redimensionado)

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
