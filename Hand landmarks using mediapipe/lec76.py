import cv2 as c 
import time 
import mediapipe

# result = cv2.VideoWriter("handlandmarks.avi" ,cv2. Videowriter_fourcc ( *'XVID' ) ,30, (640,480))

cam =c.VideoCapture(0)

mphands = mediapipe.solutions.hands
hands = mphands.Hands()
mpDraw = mediapipe.solutions.drawing_utils

pT = 0
cT=0
while True:
    _,frame = cam.read()
    fame = c.flip(frame,1)
    frameRGB = c.cvtColor(frame,c.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for idd,lm in enumerate(handLms.landmark):
                h,w,c2 = frame.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                if idd == 0:
                    c.circle(frame,(cx,cy),9,(0,255,0),c.FILLED)
                mpDraw.draw_landmarks(frame,handLms,mphands.HAND_CONNECTIONS)
    cT = time.time()
    fps = 1/(cT - pT)
    pT = cT
    c.putText(frame,str(int(fps)),(15,60),c.FONT_HERSHEY_SIMPLEX,1,(255,25,0))
    c.imshow("frame",frame)
    if c.waitKey(1) == 27:
        break
cam.release()
c.destroyAllWindows()