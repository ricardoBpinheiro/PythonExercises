# Point(x=1105, y=367)
# clicar 499 vezes
import pyautogui
import time

i = 0
time.sleep(2)
while i < 10000:
    pyautogui.click(1105, 367)
    pyautogui.hotkey('q')
    i += 1
print(' Acabou')
