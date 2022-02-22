import cv2
import mediapipe as mp
import time
import pyautogui

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.005
cap = cv2.VideoCapture(0)
 
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

sure = 0
uproll = 0
downroll = 0
 
pTime = 0
cTime = 0
lm8y = 0
lm4y = 0
thumb1 = 0
thumb3 = 0
thumbUp = 0
Lock = 0
firstfinger1 =0
firstfinger3 =0
middlefinger1 =0
middlefinger3 =0
ringfinger1 =0
ringfinger3 =0
lmx = 0
lmy = 0
lmx2 = 0
lmy2 = 0
countx =0
county =0
while True:
    success, img = cap.read()
    #反转
    img= cv2.flip(img,1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
 
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                


                
                #伸出食指
                if(id==8):
                    firstfinger1=lm.y
                    #print(lm.y)
                if(id==6):
                    firstfinger3=lm.y
                    #print(lm.y)
                #伸出中指
                if(id==12):
                    middlefinger1=lm.y
                    #print(lm.y)
                if(id==10):
                    middlefinger3=lm.y
                    #print(lm.y)
                #伸出无名指
                if(id==16):
                    ringfinger1=lm.y
                    #print(lm.y)
                if(id==14):
                    ringfinger3=lm.y
                    #print(lm.y)

                #拇指
                if(id==4):
                    thumb1=lm.y
                    if(thumb1<firstfinger1 and thumb1<middlefinger1 and thumb1<ringfinger1):
                        thumbUp=thumbUp+1
                        #print(thumbUp)
                        if thumbUp>50:
                            if Lock ==0:
                                Lock =1
                            else:
                                Lock =0
                            print(Lock)
                            pyautogui.moveRel(0, -30, duration=0.01)
                            thumbUp=0
                        
                        

                if Lock == 0:
                    if(id==17):
                        currentMouseX, currentMouseY = pyautogui.position()
                        pyautogui.moveTo(currentMouseX, currentMouseY, duration=0.01)
                        lmx=lm.x-0.5
                        lmy=lm.y-0.5
                        #滑鼠移动
                        if(firstfinger1<firstfinger3 and middlefinger1>middlefinger3 and ringfinger1>ringfinger3):

                            xmove = (lmx-lmx2)*1920*1.5
                            ymove = (lmy-lmy2)*1600*1.5
                            if(xmove>1910):
                                xmove=1910
                            if(ymove>1590):
                                ymove=1590

                            pyautogui.moveRel(xmove, ymove, duration=0.01)
                            sure = 0
                            uproll = downroll = 0
                            #print(lm.x)

                        #滑鼠确定 拳头
                        if(firstfinger1>firstfinger3*0.99 and middlefinger1>middlefinger3 and ringfinger1>ringfinger3):
                            if sure == 0 :
                                pyautogui.click()
                                sure = 1

                        #滑鼠右键 两只手指
                        if(firstfinger1<firstfinger3 and middlefinger1<middlefinger3*0.95 and ringfinger1>ringfinger3):
                            if sure == 0 :
                                pyautogui.rightClick()
                                sure = 1
                        

                        #滑鼠拖移 OK
                        if(firstfinger1>firstfinger3 and middlefinger1<middlefinger3 and ringfinger1<ringfinger3):
                            if sure == 0 :
                                pyautogui.mouseDown()
                                sure = 1
                            
                            xmove = (lmx-lmx2)*1920*1.5
                            ymove = (lmy-lmy2)*1600*1.5
                            if(xmove>1910):
                                xmove=1910
                            if(ymove>1590):
                                ymove=1590

                            pyautogui.moveRel(xmove, ymove, duration=0.01)
                        

                        #滑鼠放开
                        if(firstfinger1<firstfinger3 and middlefinger1<middlefinger3 and ringfinger1<ringfinger3):
                            pyautogui.mouseUp()
                            sure = 0
                            if lmy<0:
                                uproll=uproll+1
                            if uproll>30:
                                print("up")
                                pyautogui.press('pageup')
                                uproll = 0
                            if lmy>0.2:
                                downroll=downroll+1
                            if downroll>30:
                                print("down")
                                pyautogui.press('pagedown')
                                downroll = 0
                                
                        
                        lmx2=lmx
                        lmy2=lmy
                            

                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y*h)
                #if id ==0:
                cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
 
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
 
 
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
 
    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
 
    cv2.imshow("Image", img)
    cv2.waitKey(1)

        # 点击窗口X按钮关闭窗口，窗口名字要对应
    if cv2.getWindowProperty('Image',cv2.WND_PROP_VISIBLE) < 1:        
       break 
