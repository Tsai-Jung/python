import cv2
import numpy as np
import time
import os
import mediapipe as mp
import win32api,win32con

folderPath = "Header"
myList = os.listdir(folderPath)
print(myList)
overlayList =[]
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))

header =overlayList[0]
drawColor = (255,0,255)

#笔刷粗度
brushThickness=15
eraseThickness=80


cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)
xp,yp = 0,0
imgCanvas = np.zeros((720,1280,3),np.uint8)
 
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils
 
pTime = 0
cTime = 0
lmx = []
lmy = []
for i in range(0,21):
    lmx.append(0)
    lmy.append(0)

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
                h, w, c = img.shape
                
                lmx[id]=int(lm.x*w)
                lmy[id]=int(lm.y*h)

                #print(id,lm)
                cx, cy = int(lm.x *w), int(lm.y*h)
                #if id ==0:
                cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
 
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
 
    #两指起
        if(lmy[8]<lmy[7] and lmy[12]<lmy[11] and lmy[18]<lmy[20]):
            xp,yp = 0,0
            #确认颜色
            if lmy[8]<125:
                if 10<lmx[8]<135:
                    header = overlayList[1]
                    drawColor = (36,28,236)
                elif 170<lmx[8]<300:
                    header = overlayList[2]
                    drawColor = (39,127,255)
                elif 330<lmx[8]<460:
                    header = overlayList[3]
                    drawColor = (0,242,255)
                elif 500<lmx[8]<620:
                    header = overlayList[4]
                    drawColor = (69,209,14)
                elif 660<lmx[8]<780:
                    header = overlayList[5]
                    drawColor = (251,255,140)
                elif 820<lmx[8]<940:
                    header = overlayList[6]
                    drawColor = (243,168,0)
                elif 980<lmx[8]<1090:
                    header = overlayList[7]
                    drawColor = (54,54,54)
                elif 1140<lmx[8]<1250:
                    header = overlayList[8]
                    drawColor = (0,0,0)
            #cv2.rectangle(img,(lmx[8],lmy[8]-25),(lmx[12],lmy[12]+25),drawColor,cv2.FILLED)
                    


    #食指起
        if(lmy[8]<lmy[7] and lmy[10]<lmy[12] and lmy[18]<lmy[20]):
            cv2.circle(img,(lmx[8],lmy[8]),15,drawColor,cv2.FILLED)

            
            if xp==0 and yp ==0:
                xp,yp=lmx[8],lmy[8]
            cv2.line(img,(xp,yp),(lmx[8],lmy[8]),drawColor,brushThickness)
            cv2.line(imgCanvas,(xp,yp),(lmx[8],lmy[8]),drawColor,brushThickness)
            if drawColor == (0,0,0):
                cv2.line(img,(xp,yp),(lmx[8],lmy[8]),drawColor,eraseThickness)
                cv2.line(imgCanvas,(xp,yp),(lmx[8],lmy[8]),drawColor,eraseThickness)
                cv2.circle(img,(lmx[8],lmy[8]),50,(255,255,255),cv2.FILLED)
            
            xp,yp=lmx[8],lmy[8]
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime


    imgGray =cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY)
    _,imgInv = cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)
    imgInv =cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img =cv2.bitwise_and(img,imgInv)
    img=cv2.bitwise_or(img,imgCanvas)


    
    img[0:125,0:1280] = header
 
    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    #img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    # 调整窗口大小
    cv2.namedWindow("Image", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一直
    cv2.resizeWindow("Image", win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN))    # 设置长和宽
    cv2.imshow("Image", img)
    #cv2.imshow("Canvas", imgCanvas)
    cv2.waitKey(1)
    
    # 点击窗口X按钮关闭窗口，窗口名字要对应
    if cv2.getWindowProperty('Image',cv2.WND_PROP_VISIBLE) < 1:        
       break 
