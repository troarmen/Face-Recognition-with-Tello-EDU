from djitellopy import tello
import cv2

def initializeTello():
    drone = tello.Tello()
    drone.connect()
    print(drone.get_battery())
    drone.streamon()
    return drone

def telloGetFrame(drone, w=360, h=240):
    frame = drone.get_frame_read()
    frame = frame.frame
    return frame

