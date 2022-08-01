#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


import mediapipe as mp


# In[3]:


import pyautogui


# In[4]:


cap=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y=0
while True:
    ret, frame=cap.read()
    frame=cv2.flip(frame,1)
    frame_height,frame_width,_=frame.shape
    rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id, landmark in enumerate (landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    index_x=screen_width/frame_width*x
                    index_y=screen_height/frame_height*x
                    
                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,355,355))
                    thumb_x=screen_width/frame_width*x
                    thumb_y=screen_height/frame_height*x 
                    print('outside', abs(index_y-thumb_y))
                    if abs(index_y-thumb_y)<20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    elif abs(index_y - thumb_y) < 100:
                        pyautogui.moveTo(index_x, index_y)
    
    cv2.imshow('virtual mouse',frame)
    key=cv2.waitKey(1)
    if key == ord("b"):
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




