from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.streamon()

while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (320,240))
    cv2.imshow("Image", img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
