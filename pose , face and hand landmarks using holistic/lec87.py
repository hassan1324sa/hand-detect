import mediapipe as mp 
import cv2 
import numpy as np

mp_drawing = mp.solutions.drawing_utils 
mp_holistic = mp.solutions.holistic 

cam = cv2.VideoCapture(0)
holistic = mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame, (800, 600))
    h,w,c =frame.shape
    img = np.zeros([h,w,c])
    img.fill(0)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame.flags.writeable =False
    results = holistic.process(frame_rgb)
    # print(results.face_landmarks)
    frame.flags.writeable = True
    mp_drawing.draw_landmarks(frame, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS,      #FACEMESH_CONTOURS 
                                 mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                                 mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                                 )
    mp_drawing.draw_landmarks(img, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS,      #FACEMESH_CONTOURS 
                                 mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                                 mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                                 )
        # 2. Right hand
    mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4),
                                 mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                                 )
    mp_drawing.draw_landmarks(img, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4),
                                 mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                                 )

        # 3. Left Hand
    mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                                 mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                                 )
    mp_drawing.draw_landmarks(img, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                                 mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                                 )

        # 4. Pose Detections
    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                 )
    mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                 )
                        
    cv2.imshow('Raw Webcam Feed', frame)
    cv2.imshow('Raw Webcam Fesded', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()