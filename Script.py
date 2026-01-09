from logging import currentframe

import cv2
import os

video = cv2.VideoCapture(r'E:\thewa\video\2.mp4')
current_frame = 0

if not video.isOpened():
    print("❌ Error: Could not open video file")
    exit()

if not os .path.exists('data'):
    os.makedirs('data')

while(True):
    success,frame = video.read()

    if not success:
        print("✅ Video finished or failed to read frame")
        break

    cv2.imshow("Output",frame)
    cv2.imwrite('./data/frame'+str(current_frame)+'.jpg',frame)
    current_frame +=1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()