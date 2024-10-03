from easytello import tello

ardziv = tello.Tello()
print(ardziv.get_battery())

ardziv.takeoff()
ardziv.land()

