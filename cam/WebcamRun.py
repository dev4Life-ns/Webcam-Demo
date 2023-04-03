import cv2

# example webcam code display webcam Windows user presses x to close window
cam = cv2.VideoCapture(0)

while True:
    b, img = cam.read()
    if b:
        cv2.imshow("Window", img)
        cv2.waitKey(1)
    else:
        print("camera not working")
        break

cam.release()
cv2.destroyAllWindows()

while True:
    img = cam.read()
    if b:
        cv2.imshow('Window', img)
        cv2.waitKey(1)
