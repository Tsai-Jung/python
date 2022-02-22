import cv2
import mediapipe as mp
import time
import os
import random

def video_ope(file):
    Frame = 0
    switch = True
    cap = cv2.VideoCapture(file)
    myface_detection = mp.solutions.face_detection
    myDraw = mp.solutions.drawing_utils
    face_detection = myface_detection.FaceDetection()
    
    while(True):
        ret, img = cap.read()
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_detection.process(img_rgb)
        if (results.detections):
            for id,detection in enumerate(results.detections):
                print(detection.location_data.relative_bounding_box)
                bboxc = detection.location_data.relative_bounding_box
                h,w,c  = img.shape
                bbox = int(bboxc.xmin*w),int(bboxc.ymin*h),int(bboxc.width*w),int(bboxc.height*h)
                cv2.rectangle(img,bbox,(255,255,0),2)
                cv2.putText(img,f'FPS:{int(detection.score[0]*100)}%',(bbox[0],bbox[1]-20),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),2)            

        Frame+=1
        cv2.putText(img,str(int(Frame)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow("Frame", img)

        key = cv2.waitKey(1) & 0xFF
        if key== ord('q'):
            cv2.waitKey(0)
        if key== 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    file = 0
    video_ope(file)

if __name__=="__main__":
    main()
