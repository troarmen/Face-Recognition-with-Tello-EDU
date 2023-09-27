import cv2

face = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
olho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

imagem = cv2.imread('imagem2.png')
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = face.detectMultiScale(imagemcinza)

for (x, y, w, h) in faces:
    retanguloFace = cv2.rectangle(imagem, (x, y), (x + w, y + h), (255, 0, 255), 2)
    localOlho = retanguloFace[y:y + h, x:x + w]
    localOlhoCinza = cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY)
    detetctado = olho.detectMultiScale(localOlhoCinza, 1.3, 9)

    for (ox, oy, ol, oa) in detetctado:
        cv2.rectangle(localOlho, (ox, oy), (ox + ol, oy + oa), (255, 0, 0), 2)

imgredimensionada = cv2.resize(imagem, (620, 480))
cv2.imshow('faces', imgredimensionada)
cv2.waitKey()
