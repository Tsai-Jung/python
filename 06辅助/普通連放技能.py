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

def timecllock(num)
    num1=num*10
    num2=1
    while num2<num1 :
        time.sleep(0.1)
        num2 = num2 +1

def on_press(key):
        time1=0.9
        time2=0.2
        time3=0
        time4=0.3
        try:
            print(key.char)
            if key.char == 'r':
                print('小招')
                pyautogui.press('4')
                time.sleep(time4)
                pyautogui.press('y')
                time.sleep(time1)
                pyautogui.press('3')
                time.sleep(time4)
                pyautogui.press('y')
                time.sleep(time1)
                pyautogui.press('2')
                time.sleep(time4)
                pyautogui.press('y')
                time.sleep(time1)
                pyautogui.press('1')
                time.sleep(time4)
                pyautogui.press('y')

                

            if key.char == 'e':
                print('连招')
                pyautogui.press('2')
                time.sleep(time2)
                pyautogui.click()
                time.sleep(time4)
                pyautogui.click()
                time.sleep(time4)
                pyautogui.click()
                time.sleep(time4)
                pyautogui.click()
                time.sleep(time4)
                pyautogui.click()
                time.sleep(time2)
                pyautogui.press('1')
                time.sleep(time2)
                pyautogui.click()
                time.sleep(time4)
                pyautogui.click()
                time.sleep(time4)
                pyautogui.click()
                time.sleep(time4)
                pyautogui.click()
                time.sleep(time4)
                pyautogui.click()
                time.sleep(time2)
                
                
            if key.char == 'q':
                print('大招')
                pyautogui.press('4')
                time.sleep(time4)
                pyautogui.press('t')
                time.sleep(time1)
                pyautogui.press('3')
                time.sleep(time4)
                pyautogui.press('t')
                time.sleep(time1)
                pyautogui.press('2')
                time.sleep(time4)
                pyautogui.press('t')
                time.sleep(time1)
                pyautogui.press('1')
                time.sleep(time4)
                pyautogui.press('t')                        
                    

                                

                
        except AttributeError:
            print('special key {0} pressed'.format(key))
            print(key)
            if key == 'Key.f2':
                print('cool')
 
 
while True:
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()
