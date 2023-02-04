#this is a screenshot app that takes a screenshot of the screen and saves it to a file


import pyautogui
import time

#take screenshot
time.sleep(5)
img = pyautogui.screenshot()

#save the image

img.save('C:/Users/USER/Pictures/Screenshots/screenshot.png')

