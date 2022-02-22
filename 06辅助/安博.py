from pynput import keyboard
import pyautogui
import time


key2 = 0
def on_press(key):
        time1=0.9
        time2=0.2
        time3=0
        try:
            print(key.char)
            if key.char == 'r':
                print('换角色')
                pyautogui.press('2')
                time.sleep(time2)
                pyautogui.press('e')
                time.sleep(time1)
                pyautogui.press('3')
                time.sleep(time2)
                pyautogui.press('e')
                time.sleep(time1)
                pyautogui.press('4')
                time.sleep(time2)
                pyautogui.press('e')
                time.sleep(time1)
                pyautogui.press('1')
                time.sleep(time2)
                
                
            if key.char == 't':
                pyautogui.press('2')
                time.sleep(0.2)
                pyautogui.press('q')
                time.sleep(1)
                pyautogui.press('3')
                time.sleep(0.2)
                pyautogui.press('q')
                time.sleep(1)
                pyautogui.press('4')
                time.sleep(0.2)
                pyautogui.press('q')
                time.sleep(1)
                pyautogui.press('1')
                time.sleep(0.2)
                pyautogui.press('q')
                time.sleep(0.2)

                
        except AttributeError:
            print('special key {0} pressed'.format(key))
            print(key)
            if key == 'Key.f2':
                print('cool')
 
 
while True:
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()
