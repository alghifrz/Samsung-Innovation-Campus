import cv2
import numpy as np
import requests

SERVER_URL = 'http://localhost:5000/sensor_data'

def send_data_to_server(data):
    response = requests.post(SERVER_URL, json={'sensor_data': data.tolist()})
    if response.status_code == 200:
        print('Data berhasil dikirim:', response.json())
    else:
        print('Gagal mengirim data:', response.text)

def detect_motion(frame, background):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(gray_background, gray_frame)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

cap = cv2.VideoCapture(0)
ret, background = cap.read()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    contours = detect_motion(frame, background)
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            motion_data = np.array([x, y, w, h])
            send_data_to_server(motion_data)

    cv2.imshow('Motion Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ret, background = cap.read()

cap.release()
cv2.destroyAllWindows()
