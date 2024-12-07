# Face-Recognition-with-Tello-EDU
This is a study repository for Image Processing and Facial Recognition in Drones (specifically the Tello EDU).

### The following files are modules containing functions used in the controllers:
- `functions.py`
- `keyboardpress.py`
- `KeyPressModule.py`

## Controllers

### `keyboard_controller.py`:
Allows you to control the drone via keyboard.

### `keyboard_controller_image.py`:
Controls the drone, displays the real-time camera feed, and allows you to capture frames.

### `graphical_controller.py`:
Graphical controller using Tkinter.

## Recognizers

### `recognizer_face_using_image.py`:
Recognizes faces in a provided image.

### `recognizer_notebook_camera.py`:
Recognizes faces using the notebook camera.

### `recognizer_faceneye_tello.py`:
Recognizes faces and eyes using the Tello EDU camera.

### `recognizer_faceneye_using_image.py`:
Recognizes faces and eyes in a provided image.

### `recognizer_faceneye_notebook_camera.py`:
Recognizes faces and eyes using the notebook camera.

## Haarcascades

This project uses two different Haarcascades: one for face detection and another for eye detection.  
Both are located in the folder: `/haarcascades`

