from pynput import keyboard
import pyautogui
import time
import win32api
import win32con

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.005

key2 = 0
def mouse_move(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)

def count(num):
    time_start=time.time()
    
    while (time.time()-time_start < num):
       a=1;
       

def on_press(key):
        time1=0.9
        time2=0.2
        time3=0
        time4=0.3
        try:
            print(key.char)
            if key.char == 'r':
                print('小招')
                pyautogui.press('y')
                count(time1)
                pyautogui.press('4')
                count(time4)
                pyautogui.press('y')
                count(time1)
                pyautogui.press('3')
                count(time4)
                pyautogui.press('y')
                count(time1)
                pyautogui.press('2')
                count(time4)
                pyautogui.press('y')
                count(time1)
                pyautogui.press('1')
                

                

            if key.char == 'e':
                print('小招2')
                pyautogui.press('4')
                count(time4)
                pyautogui.press('y')
                count(time1)
                pyautogui.press('3')
                count(time4)
                pyautogui.press('y')
                count(time1)
                pyautogui.press('2')
                count(time4)
                pyautogui.press('y')
                count(time1)
                pyautogui.press('1')
                
                
            if key.char == 'q':
                print('大招')
                pyautogui.press('4')
                count(time4)
                pyautogui.press('t')
                count(1)
                pyautogui.press('3')
                count(time4)
                pyautogui.press('t')
                count(1)
                pyautogui.press('2')
                count(time4)
                pyautogui.press('t')
                count(1)
                pyautogui.press('1')
                count(time4)
                pyautogui.press('t')
                count(time2)                          
                    

                                

                
        except AttributeError:
            print('special key {0} pressed'.format(key))
            print(key)
            if key == 'Key.f2':
                print('cool')
 
 
while True:
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()
