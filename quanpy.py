import time
import pyautogui
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
pyautogui.click(781,1048)
time.sleep(5)
pyautogui.write('facebook.com', interval=0.25)
pyautogui.press('enter')
time.sleep(7)
pyautogui.click(1025,688)
time.sleep(10)
pyautogui.write('kia co tay lap lanh cartier ', interval=0.25)
pyautogui.click(951,827)
