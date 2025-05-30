import time
import cv2 as cv
from ultralytics import YOLO
#import os
#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
model = YOLO('yolov8x-oiv7.pt')
import matplotlib.pyplot as plt
plt.ioff()
#cap = cv.VideoCapture(0)

#path = 'http://192.168.0.103:8080/video'
rtsp_url = 'rtsp://192.168.0.117/'
#path = 'http://192.168.0.181/'
cap = cv.VideoCapture(rtsp_url)

def fps(start, end):
    return int(1//(end-start))

try:
    while cap.isOpened():
        ret, image = cap.read()
        if not ret:
            print('No camera detected, aborting')
            break
        start = time.perf_counter()
        results = model(image)
        end = time.perf_counter()
        segments = results[0].plot()
        cv.putText(segments, f'FPS: {fps(start, end)}', (10, 30),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv.imshow('Image Segmentation', segments)

        key = cv.waitKey(1)
        if key & 0xFF == ord('q'):
            print('Exit sequence initiated')
            break

finally:
    cap.release()
    cv.destroyAllWindows()