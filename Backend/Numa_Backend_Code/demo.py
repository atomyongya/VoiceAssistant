#!/usr/bin/python3
import os

# os.system("sudo apt update\nsudo apt upgrade\nsudo apt autoremove")


import pyautogui,time

pyautogui.keyDown('alt')
# time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')