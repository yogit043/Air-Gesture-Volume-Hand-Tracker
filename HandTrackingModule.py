import cv2
import mediapipe as mp
import time

class handDetector():
    
    def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            model_complexity=self.modelComplexity,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        
    def findHands(self , img , draw = True):
        imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks: # iterates over each detected hand.
                if draw:
                    self.mpDraw.draw_landmarks(img , handLms , self.mpHands.HAND_CONNECTIONS) # This draws the landmarks and connections between them on the image.
        return img
    
    def findPosition(self , img , handNo = 0 , draw = True):
        
        lmList = []
        
        if self.results.multi_hand_landmarks:
            self.myHand = self.results.multi_hand_landmarks[handNo]
            for id , lm in enumerate(self.myHand.landmark):  # iterates over each landmark in the hand.
                # print(id , lm)
                h , w, c = img.shape
                cx , cy = int(lm.x*w) , int(lm.y*h)
                # print(id , cx , cy)
                lmList.append([id , cx ,cy])
                # if id==0:
                if draw:
                    cv2.circle(img , (cx,cy) , 10 , (255,0,255) , cv2.FILLED)
        return lmList
    
    
def main():
    
    prevTime = 0
    currTime = 0
    cap = cv2.VideoCapture(0 , cv2.CAP_DSHOW)
    detector = handDetector()
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
        
if __name__ == "__main__":
    main()