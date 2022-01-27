import datetime
import cv2
import os

capture = cv2.VideoCapture("rtsp://admin:1234556@10.252.11.35/stream0")

path = ".\\image\\Area05_2"
if not os.path.isdir(path):
    os.mkdir(path)

while True:
    ret, image = capture.read()

    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nowHour = datetime.datetime.now().strftime("%H")
    nowMinute = datetime.datetime.now().strftime("%M")
    nowSecond = datetime.datetime.now().strftime("%S")
    print(str(now))

    if nowMinute == "00" and nowSecond == "00":
        try:
            cv2.imwrite("image\\Area05_2\\Parking_Area05_2_" + str(now) + ".png", image)
        except:
            cv2.imwrite("image\\Area05_2\\Parking_Area05_2_" + str(now) + ".png", image)
    elif nowMinute == "15" and nowSecond == "00":
        try:
            cv2.imwrite("image\\Area05_2\\Parking_Area05_2_" + str(now) + ".png", image)
        except:
            cv2.imwrite("image\\Area05_2\\Parking_Area05_2_" + str(now) + ".png", image)
    elif nowMinute == "30" and nowSecond == "00":
        try:
            cv2.imwrite("image\\Area05_2\\Parking_Area05_2_" + str(now) + ".png", image)
        except:
            cv2.imwrite("image\\Area05_2\\Parking_Area05_2_" + str(now) + ".png", image)
    elif nowMinute == "45" and nowSecond == "00":
        try:
            cv2.imwrite("image\\Area05_2\\Parking_Area05_2_" + str(now) + ".png", image)
        except:
            cv2.imwrite("image\\Area05_2\\Parking_Area05_2_" + str(now) + ".png", image)
