import cv2
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
cap.set(3, 1000)
cap.set(4, 600)

detector = cv2.QRCodeDetector()

while cap.isOpened():
    # READ frames of video
    success, image = cap.read()

    if not success:
        print('Skipping empty frame.')
    # start decoding qrcode
    decodedObjects = pyzbar.decode(image)
    # Background rectangle to display text
    cv2.rectangle(image, (0, 0), (1000, 80), (245, 176, 66), -1)

    for obj in decodedObjects:
        data = obj.data.decode('utf-8')

        # Display data in qr code
        cv2.putText(image, data, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 250), 2)

        x, y, w, h = obj.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 250, 0), 2)

     # Show live webcam feed
    cv2.imshow('QR CODE SCANNER', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()