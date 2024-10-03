import cv2

upload = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt2.xml')

imagem = cv2.imread('../images/imagem2.png')
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = upload.detectMultiScale(imagemcinza, scaleFactor=1.75, minNeighbors=1, minSize=(120, 120))
print(faces)
for x, y, w, h in faces:
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)

imgredimensionada = cv2.resize(imagem, (620, 480))
cv2.imshow('faces', imgredimensionada)
cv2.waitKey()

"""while True:
    cv2.imshow('imagem', imagemcinza)
    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break
cv2.destroyAllWindows()"""