import pyautogui
import time

pyautogui.press('Win')
time.sleep(2)
pyautogui.write('Youtube')
time.sleep(2)
pyautogui.press('enter')
time.sleep(4)
pyautogui.hotkey('Ctrl','t')
time.sleep(4)
pyautogui.write('https://www.youtube.com/watch?v=C5ZFFJUNco4')
time.sleep(2)
pyautogui.press('enter')