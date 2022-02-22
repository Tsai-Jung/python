import cv2
import mediapipe as mp
import time


mpDraw = mp.solutions.drawing_utils
mpPose =mp.solutions.pose
pose = mpPose.Pose()


cap = cv2.VideoCapture(2)
pTime=0

while True:
    success,img =cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    #print(results.pose_landmarks)
    if results.pose_landmarks :
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id,lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            #print(id, lm.x,lm.y)#查询各个点的坐标
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)



    
    cTime = time.time()
    fps=1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    # 调整窗口大小
    cv2.namedWindow("Image", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一直

    cv2.resizeWindow("Image", 1600, 900)    # 设置长和宽

    cv2.imshow('Image',img)
    cv2.waitKey(1)
    
