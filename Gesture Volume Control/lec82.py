import cv2 as c 
import numpy as np 
import math
from pynput.keyboard import Key,Controller
import mediapipe


keyboard = Controller()

wCam , hCam = 1280,720

cam =c.VideoCapture(0)

cam.set(3,wCam)
cam.set(4,hCam)

mphands = mediapipe.solutions.hands
hands = mphands.Hands()
mpDraw = mediapipe.solutions.drawing_utils

lastAngle = None
lastLength = None

minAngle = -95
maxAngle = 0
angle =0 
angleBar = 400
angleDeg = 0
minHand = 50
maxHand = 300
length = 0
while True:
    success,frame = cam.read()
    frame = c.flip(frame,1)
    frameRGB = c.cvtColor(frame,c.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    lmList = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for idd,lm in enumerate(handLms.landmark):
                h,w,c2 = frame.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
                mpDraw.draw_landmarks(frame,handLms,mphands.HAND_CONNECTIONS)
    
    if len(lmList) != 0:
        x1,y1 = lmList[4][1] ,lmList[4][2]
        x2,y2 = lmList[8][1] ,lmList[8][2]
        cx,cy =(x1+x2) // 2, (y1+y2) // 2 
        c.circle(frame,(x1,y1),15,(0,0,255),c.FILLED)
        c.circle(frame,(x2,y2),15,(0,0,255),c.FILLED)
        c.line(frame,(x1,y1),(x2,y2),(0,0,255),3)
        c.circle(frame,(cx,cy),15,(0,0,255,),c.FILLED)
        length=math.hypot(x2-x1,y2-y1)
        angle = np.interp(length,[minHand,maxHand],[minAngle,maxAngle])
        angleBar = np.interp(length,[minHand,maxHand],[400,150])
        angleDeg = np.interp(length,[minHand,maxHand],[0,100])
        
        if length < 50 :
            c.circle(frame,(cx,cy),15,(0,255,0),c.FILLED)
    c.rectangle(frame,(50,150),(85,400),(255,0,0),3)
    c.rectangle(frame,(50,int(angleBar)),(85,400),(255,0,0),c.FILLED)
    c.putText(frame, f'{int(angleDeg)} %',(40,120),c.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)
    if lastLength:
        if length > lastLength:
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
        elif length < lastLength:
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
    lastAngle = angle
    lastLength = length
    c.imshow("asd",frame)
    if c.waitKey(1) == 27:
        break
c.destroyAllWindows()
cam.release()