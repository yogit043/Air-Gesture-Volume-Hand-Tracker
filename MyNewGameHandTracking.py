import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

prevTime = 0
currTime = 0
cap = cv2.VideoCapture(0 , cv2.CAP_DSHOW)
detector = htm.handDetector()
while True:
    success , img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) !=0:
        print(lmList[4]) # tip of the thumb
    cTime = time.time()
    fps = 1/(cTime-prevTime)
    prevTime = cTime
    
    cv2.putText( img , str(int(fps)) , (10,70) , cv2.FONT_HERSHEY_PLAIN , 3 , (255,0,255) , 3)
    
    
    cv2.imshow("Image" ,img)
    cv2.waitKey(1)
