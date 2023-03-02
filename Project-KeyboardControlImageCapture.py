import cv2
from djitellopy import tello
import KeyPressModule as kp
import time


kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
global img
me.streamon()
xml_haar_cascade = 'haarcascade_frontalface_alt2.xml'
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 70

    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = -speed
    elif kp.getKey("d"):
        yv = speed

    if kp.getKey("e"):
        me.takeoff()
    if kp.getKey("q"):
        me.land()

    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)  # Delay para adicionado para que não se salve vários frames

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceClassifier.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
    img = cv2.resize(img, (320, 240))
    cv2.imshow('Image', img)
    cv2.waitKey(1)
