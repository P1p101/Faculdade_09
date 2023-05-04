import pyautogui
import time

pyautogui.press('Win')
time.sleep(2)
pyautogui.write('Google')
time.sleep(3)
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('Ctrl', 't')
time.sleep(2)
pyautogui.write('https://chat.openai.com/')
time.sleep(2)
pyautogui.press('enter')
