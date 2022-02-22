import cv2
import mediapipe as mp
import time
import pyautogui
import win32api
import win32con

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.005

def mouse_move(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)


mpDraw = mp.solutions.drawing_utils
mpPose =mp.solutions.pose
pose = mpPose.Pose()


cap = cv2.VideoCapture(0)
pTime=0
##############################
#身体部位
time1=0.9
time2=0.2
num=0
num1=0
num2=0
num3=0
lock = 0
lockwalk =0
#鼻子
nose = [0,0,0]
nose1=[0,0,0]
nose2=[0,0,0]
nose3=[0,0,0]

#左眉毛
leftinner=[0,0,0]
leftinner1=[0,0,0]
leftinner2=[0,0,0]
leftinner3=[0,0,0]
#右眉毛
rightinner=[0,0,0]
rightinner1=[0,0,0]
rightinner2=[0,0,0]
rightinner3=[0,0,0]

#左耳
leftear=[0,0,0]
leftear1=[0,0,0]
leftear2=[0,0,0]
leftear3=[0,0,0]
#右耳
rightear=[0,0,0]
rightear1=[0,0,0]
rightear2=[0,0,0]
rightear3=[0,0,0]

#左手
lefthand=[0,0,0]
lefthand1=[0,0,0]
lefthand2=[0,0,0]
lefthand3=[0,0,0]
#右手
righthand=[0,0,0]
righthand1=[0,0,0]
righthand2=[0,0,0]
righthand3=[0,0,0]

#左手轴
leftelbow=[0,0,0]
leftelbow1=[0,0,0]
leftelbow2=[0,0,0]
leftelbow3=[0,0,0]

#右手轴
rightelbow=[0,0,0]
rightelbow1=[0,0,0]
rightelbow2=[0,0,0]
rightelbow3=[0,0,0]

#左膝盖
leftknee=[0,0,0]
leftknee1=[0,0,0]
leftknee2=[0,0,0]
leftknee3=[0,0,0]
#右膝盖
rightknee=[0,0,0]
rightknee1=[0,0,0]
rightknee2=[0,0,0]
rightknee3=[0,0,0]

#左脚踝
leftheel=[0,0,0]
leftheel1=[0,0,0]
leftheel2=[0,0,0]
leftheel3=[0,0,0]
#右脚踝
rightheel=[0,0,0]
rightheel1=[0,0,0]
rightheel2=[0,0,0]
rightheel3=[0,0,0]

#左腰
lefthip=[0,0,0]
lefthip1=[0,0,0]
lefthip2=[0,0,0]
lefthip3=[0,0,0]
#右腰
righthip=[0,0,0]
righthip1=[0,0,0]
righthip2=[0,0,0]
righthip3=[0,0,0]


noseall = [nose1,nose2,nose3]
leftearall = [leftear1,leftear2,leftear3]



##############################
while True:
    success,img =cap.read()
    #反转
    img= cv2.flip(img,1)
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    #print(results.pose_landmarks)
    if results.pose_landmarks :
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id,lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            #print(id, lm.x,lm.y)#查询各个点的坐标
            cx, cy, cz= int(lm.x * w), int(lm.y * h), lm.z
            #侦测鼻子
            if(id==0):
                nose=cx,cy,cz
                #print(cx,cy,cz)

            #侦测左眉毛
            if(id==4):
                leftinner=cx,cy,cz
                #print(cx,cy,cz)
            #侦测右眉毛
            if(id==1):
                rightinner=cx,cy,cz
                #print(cx,cy,cz)
            #侦测左耳
            if(id==8 ):
                leftear=cx,cy,cz
                #print(cx,cy,cz)
            #侦测右耳
            if(id==7 ):
                rightear=cx,cy,cz
                #print(cx,cy,cz)
            #侦测左手
            if(id==16 ):
                lefthand=cx,cy,cz
                #print(cx,cy,cz)
            #侦测右手
            if(id==15 ):
                righthand=cx,cy,cz
                #print(cx,cy,cz)
            #侦测左手轴
            if(id==14 ):
                leftelbow=cx,cy,cz
                #print(cx,cy,cz)
            #侦测右手轴
            if(id==13 ):
                rightelbow=cx,cy,cz
                #print(cx,cy,cz)
            #侦测左膝盖
            if(id==26 and cz>-1):
                leftknee=cx,cy,cz
                #print(cx,cy,cz)
            #侦测右膝盖
            if(id==26 and cz>-1):
                rightknee=cx,cy,cz
                #print(cx,cy,cz)
            #侦测左脚踝
            if(id==27 and cz>-1):
                leftheel=cx,cy,cz
                #print(cx,cy,cz)
            #侦测右脚踝
            if(id==28 and cz>-1):
                rightheel=cx,cy,cz
                #print(cx,cy,cz)
            #侦测左腰
            if(id==26 and cz>-1):
                lefthip=cx,cy,cz
                #print(cx,cy,cz)
            #侦测右腰
            if(id==23 and cz>-1):
                righthip=cx,cy,cz
                #print(cx,cy,cz)
            
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        if nose[2]>-0.6:
            #print(nose[2])
            
            #判断跳跃
            if num==1:
                #print("第一个")
                nose1[0:2]=nose[0:2]
                leftear1[0:2]=leftear[0:2]
                rightear1[0:2]=rightear[0:2]
                lefthip1[0:2]=lefthip[0:2]
                righthip1[0:2]=righthip[0:2]
            elif num==5:
                #print("第二个")
                nose2[0:2]=nose[0:2]
                leftear2[0:2]=leftear[0:2]
                rightear2[0:2]=rightear[0:2]
                lefthip2[0:2]=lefthip[0:2]
                righthip2[0:2]=righthip[0:2]
            elif num==9:
                #print("第三个")
                nose3[0:2]=nose[0:2]
                leftear3[0:2]=leftear[0:2]
                rightear3[0:2]=rightear[0:2]
                lefthip3[0:2]=lefthip[0:2]
                righthip3[0:2]=righthip[0:2]
            elif num==13:
                #print(nose3)
                #print(leftear3)
                #print(rightear3)
                #print(lefthip3)
                #print(righthip3)
                if(nose3[1]<nose2[1]<nose1[1] and leftear3[1]<leftear2[1]<leftear1[1]
                   and rightear3[1]<rightear2[1]<rightear1[1]
                   ):
                    print('跳跃')
                    pyautogui.keyDown('space')
                    time.sleep(0.2)
                    pyautogui.keyUp('space')
                num=0

            #判断走路
            if num1==1:
                #print("第一个")
                rightheel1[0:2]=rightheel[0:2]
                leftheel1[0:2]=leftheel[0:2]
            elif num1==2:
                #print("第二个")
                rightheel2[0:2]=rightheel[0:2]
                leftheel2[0:2]=leftheel[0:2]
            elif num1==3:
                #print("第三个")
                rightheel3[0:2]=rightheel[0:2]
                leftheel3[0:2]=leftheel[0:2]
            elif num1==4:
                if(rightheel3[1]<rightheel2[1]<rightheel1[1]):
                    print('走路')
                    pyautogui.keyDown('w')
                    lockwalk=0
                elif(leftheel3[1]<leftheel2[1]<leftheel1[1]):
                    print('走路')
                    pyautogui.keyDown('w')
                    lockwalk=0
##                elif(rightheel3[1]>rightheel2[1]>rightheel1[1]):
##                    print('走路')
##                    pyautogui.keyDown('w')
##                    lockwalk=0
                elif(leftheel3[1]>leftheel2[1]>leftheel1[1]):
                    print('走路')
                    pyautogui.keyDown('w')
                    pyautogui.press('f')
                    lockwalk=0
                else:
                    if(lockwalk==3):
                        print('停下来')
                        pyautogui.press('f')
                        time.sleep(time2)
                        pyautogui.keyUp('w')
                        lock=0
                    elif(lockwalk>3):
                        print('等待')
                    lockwalk=lockwalk+1
                    
                num1=0
                

            #判断左右转
            if num2==8:
                #print(nose)
                #print(leftear)
                if(righthand[0]<leftelbow[0]):
                    print('左转')
                    mouse_move(-300, 0)
                if(lefthand[0]>rightelbow[0]):
                    print('右转')
                    mouse_move(300, 0)
                num2=0


            #判断攻击
            if num3==1:
                #print("第一个")
                righthand1[0:2]=righthand[0:2]
                lefthand1[0:2]=lefthand[0:2]
                rightinner1[0:2]=rightinner[0:2]
                
            elif num3==4:
                #print("第二个")
                righthand2[0:2]=righthand[0:2]
                lefthand2[0:2]=lefthand[0:2]
                rightinner2[0:2]=rightinner[0:2]
            elif num3==7:
                #print("第三个")
                righthand3[0:2]=righthand[0:2]
                lefthand3[0:2]=lefthand[0:2]
                rightinner3[0:2]=rightinner[0:2]
            elif num3==8:
                #print(righthand)
                if(abs(righthand3[0]-righthand1[0])>100):
                    print('攻击')
                    pyautogui.click()
                    pyautogui.keyUp('w')
                    lock=0
                elif(abs(lefthand3[0]-lefthand1[0])>100):
                    print('攻击')
                    pyautogui.click()
                    pyautogui.press('f')
                    pyautogui.keyUp('w')
                    lock=0
                elif(righthand3[1]<rightinner3[1] and righthand2[1]<rightinner2[1] and righthand1[1]<rightinner1[1]
                     and lefthand3[1]<rightinner3[1] and lefthand2[1]<rightinner2[1] and lefthand1[1]<rightinner1[1]
                     and lock==0):
                    print('大招')
                    pyautogui.press('4')
                    time.sleep(0.2)
                    pyautogui.press('t')
                    time.sleep(1)
                    pyautogui.press('3')
                    time.sleep(0.2)
                    pyautogui.press('t')
                    time.sleep(1)
                    pyautogui.press('2')
                    time.sleep(0.2)
                    pyautogui.press('t')
                    time.sleep(1)
                    pyautogui.press('1')
                    time.sleep(0.2)
                    pyautogui.press('t')
                    time.sleep(0.2)
                    lock=1
                elif(righthand3[1]<rightinner3[1] and righthand2[1]<rightinner2[1] and righthand1[1]<rightinner1[1]
                     and lock==0):
                    print('连招')
                    pyautogui.press('2')
                    time.sleep(time2)
                    pyautogui.mouseDown(button='left')
                    time.sleep(1)
                    pyautogui.mouseUp(button='left')
                    time.sleep(time2)
                    pyautogui.press('1')
                    time.sleep(time2)
                    pyautogui.click()
                    time.sleep(time2)
                    pyautogui.click()
                    time.sleep(time2)
                    pyautogui.click()
                    time.sleep(time2)
                    pyautogui.click()
                    time.sleep(time2)
                    pyautogui.click()
                    time.sleep(time2)
                    pyautogui.keyDown('y')
                    time.sleep(2)
                    pyautogui.keyUp('y')
                    lock=1
                elif(lefthand3[1]<rightinner3[1] and lefthand2[1]<rightinner2[1] and lefthand1[1]<rightinner1[1]
                     and lock==0):
                    print('小招')
                    pyautogui.press('4')
                    time.sleep(time2)
                    pyautogui.press('y')
                    time.sleep(time1)
                    pyautogui.press('3')
                    time.sleep(time2)
                    pyautogui.press('y')
                    time.sleep(time1)
                    pyautogui.press('2')
                    time.sleep(time2)
                    pyautogui.press('y')
                    time.sleep(time1)
                    pyautogui.press('1')
                    time.sleep(time2)
                    pyautogui.keyDown('s')
                    time.sleep(time2)
                    pyautogui.keyDown('shift')
                    time.sleep(time2)
                    pyautogui.keyUp('shift')
                    time.sleep(time2)
                    pyautogui.keyUp('s')
                    time.sleep(time2)
                    pyautogui.keyDown('w')
                    time.sleep(time2)
                    pyautogui.keyUp('w')
                    lock=1
                
                    
                num3=0

                
                
            #print(noseall)
            #print(num)
            num=num+1
            num1=num1+1
            num2=num2+1
            num3=num3+1

        



    
    cTime = time.time()
    fps=1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow('Image',img)
    cv2.waitKey(1)

    # 点击窗口X按钮关闭窗口，窗口名字要对应
    if cv2.getWindowProperty('Image',cv2.WND_PROP_VISIBLE) < 1:        
       break 
    
