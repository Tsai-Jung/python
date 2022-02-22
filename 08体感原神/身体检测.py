import cv2
import mediapipe as mp
import time


mpDraw = mp.solutions.drawing_utils
mpPose =mp.solutions.pose
pose = mpPose.Pose()


cap = cv2.VideoCapture(0)
pTime=0
##############################
#身体部位
num=0
num1=0
num2=0
num3=0
lock = 0 
#鼻子
nose = [0,0,0]
nose1=[0,0,0]
nose2=[0,0,0]
nose3=[0,0,0]
#眉毛
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
            cx, cy, cz= int(lm.x * w), int(lm.y * h), int(lm.z*100)
            #侦测鼻子
            if(id==0):
                nose=cx,cy,cz
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
            #侦测左膝盖
            if(id==26 and cz>-1):
                leftknee=cx,cy,cz
                #print(cx,cy,cz)
            #侦测右膝盖
            if(id==26 and cz>-1):
                rightknee=cx,cy,cz
                #print(cx,cy,cz)
            #侦测左腰
            if(id==26 and cz>-1):
                lefthip=cx,cy,cz
                #print(cx,cy,cz)
            #侦测右腰
            if(id==26 and cz>-1):
                righthip=cx,cy,cz
                #print(cx,cy,cz)
            
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

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
        elif num==10:
            #print("第三个")
            nose3[0:2]=nose[0:2]
            leftear3[0:2]=leftear[0:2]
            rightear3[0:2]=rightear[0:2]
            lefthip3[0:2]=lefthip[0:2]
            righthip3[0:2]=righthip[0:2]
        elif num==15:
            #print(nose3)
            #print(leftear3)
            #print(rightear3)
            #print(lefthip3)
            #print(righthip3)
            if(nose3[1]<nose2[1]<nose1[1] and leftear3[1]<leftear2[1]<leftear1[1]
               and rightear3[1]<rightear2[1]<rightear1[1] and lefthip3[1]<lefthip2[1]<lefthip1[1]
               and righthip3[1]<righthip2[1]<righthip1[1]):
                print('跳跃')
            num=0

        #判断走路
        if num1==1:
            #print("第一个")
            rightknee1[0:2]=rightknee[0:2]
            leftknee1[0:2]=leftknee[0:2]
        elif num1==3:
            #print("第二个")
            rightknee2[0:2]=rightknee[0:2]
            leftknee2[0:2]=leftknee[0:2]
        elif num1==5:
            #print("第三个")
            rightknee3[0:2]=rightknee[0:2]
            leftknee3[0:2]=leftknee[0:2]
        elif num1==7:
            if(rightknee3[1]>rightknee2[1]>rightknee1[1] and rightknee[1]<1000):
                print('走路')
            elif(leftknee3[1]>leftknee2[1]>leftknee1[1] and leftknee[1]<1000):
                print('走路')
            num1=0
            

        #判断左右转
        if num2==10:
            #print(nose)
            #print(leftear)
            if(nose[0]<leftear[0]):
                print('左转')
            if(nose[0]>rightear[0]):
                print('右转')
            num2=0


        #判断攻击
        if num3==1:
            #print("第一个")
            righthand1[0:2]=righthand[0:2]
            lefthand1[0:2]=lefthand[0:2]
            rightinner1[0:2]=rightinner[0:2]
            
        elif num3==3:
            #print("第二个")
            righthand2[0:2]=righthand[0:2]
            lefthand2[0:2]=lefthand[0:2]
            rightinner2[0:2]=rightinner[0:2]
        elif num3==6:
            #print("第三个")
            righthand3[0:2]=righthand[0:2]
            lefthand3[0:2]=lefthand[0:2]
            rightinner3[0:2]=rightinner[0:2]
        elif num3==9:
            #print(righthand)
            if(abs(righthand3[0]-righthand1[0])>120):
                print('攻击')
                lock=0
            elif(abs(lefthand3[0]-lefthand1[0])>120):
                print('攻击')
                lock=0
            elif(righthand3[1]<rightinner3[1] and righthand2[1]<rightinner2[1] and righthand1[1]<rightinner1[1] and lock==0):
                print('招数一')
                lock=1
            elif(lefthand3[1]<rightinner3[1] and lefthand2[1]<rightinner2[1] and lefthand1[1]<rightinner1[1] and lock==0):
                print('招数二')
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
    
