import pyautogui
from time import sleep
#Position

#mover para
pyautogui.moveTo(487,381,duration=2)
#mover em relação a ultima posição
for i in range(1,50):
   sleep(0.1)
   pyautogui.click()