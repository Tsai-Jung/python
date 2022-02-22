from pynput import keyboard
import pyautogui
import time
import win32api
import win32con

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01
lock = 0
key2 = 0
def mouse_move(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)

def count(num):
    time_start=time.time()
    
    while (time.time()-time_start < num):
       time.sleep(0.1)

def on_press(key):
        global lock
        time1=0.9
        time2=0.2
        time3=0
        time4=0.3
        try:
            with open(r"Help.txt","r") as f:
                Word=f.read() 
            if Word=='Off':
                return False
            
            print(key.char)
            if  key.char == '`':
                if(lock == 0):
                    lock = 1
                    count(1)
                elif(lock == 1):
                    lock = 0
                    count(1)
                
                
            if  key.char == '1'  and lock==0:
                count(0.3)
                pyautogui.press('q')
                pyautogui.keyDown('e')
                count(0.8)
                pyautogui.keyUp('e')

            if  key.char == '2'  and lock==0:
                count(0.3)
                pyautogui.press('q')
                pyautogui.press('e')
                pyautogui.click()
                count(0.3)
                pyautogui.mouseDown()
                count(0.5)
                pyautogui.mouseUp()
                

            if  key.char == '3'  and lock==0:
                count(0.3)
                pyautogui.press('q')
                pyautogui.keyDown('e')
                pyautogui.click()
                count(0.3)
                pyautogui.keyUp('e')


            if  key.char == '4'  and lock==0:
                count(0.3)
                pyautogui.press('q')
                pyautogui.press('e')
                pyautogui.click()
                
##            if key.char == 'r'  and lock==0:
##                print('重击')
##                pyautogui.press('2')
##                count(time4)
##                pyautogui.click()
##                count(time4)
##                pyautogui.mouseDown()
##                count(0.8)
##                pyautogui.mouseUp()




##            if key.char == 't'  and lock==0:
##                print('大招')
##                pyautogui.press('4')
##                count(time4)
##                pyautogui.press('q')
##                pyautogui.press('e')
##                count(time1)
##                pyautogui.press('3')
##                count(time4)
##                pyautogui.press('q')
##                pyautogui.press('e')
##                count(time1)
##                pyautogui.press('2')
##                count(time4)
##                pyautogui.press('q')
##                pyautogui.press('e')
##                count(time1)
##                pyautogui.press('1')
##                count(time4)
##                pyautogui.press('q')
##                pyautogui.press('e')
                                
            
        except AttributeError:
            #print('special key {0} pressed'.format(key))
            #print(key)
            if key == 'Key.f2':
                a=1
                #print('cool')
 
 
#while True:

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()
