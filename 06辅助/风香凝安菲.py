from pynput import keyboard
import pyautogui
import time

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.005

key2 = 0
def on_press(key):
        time1=0.9
        time2=0.2
        time3=0
        try:
            print(key.char)
            if key.char == 'r':
                print('ε°ζ')
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
                

            if key.char == 'e':
                print('θΏζ')
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
                
                
            if key.char == 'q':
                print('ε€§ζ')
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

                                

                
        except AttributeError:
            print('special key {0} pressed'.format(key))
            print(key)
            if key == 'Key.f2':
                print('cool')
 
 
while True:
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()
