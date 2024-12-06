import cv2

upload = cv2.CascadeClassifier('../haarcascade_frontalface_alt2.xml')

imagem = cv2.imread('../images/imagem2.png')
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = upload.detectMultiScale(imagemcinza)
print(faces)
for x, y, w, h in faces:
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 0, 255), 2)

imgredimensionada = cv2.resize(imagem, (620, 480))
cv2.imshow('faces', imgredimensionada)
cv2.waitKey()