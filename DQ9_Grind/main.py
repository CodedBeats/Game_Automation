import cv2 as cv
import numpy as np
import pyautogui as pygui
import time
import os
import keyboard

# ======================================================== Key Press and Click Func ======================================================== #
def pressKey(key):
    pygui.keyDown(key)
    pygui.keyUp(key)


def pyClick(x,y):
    pygui.click(x,y)
    pygui.mouseDown()
    pygui.mouseUp()





# ======================================================== Attack Sequence Func ======================================================== #
def atkSeq():
    for i in range(9):
        pressKey("x")
        time.sleep(0.1)





# ======================================================== Startup Func ======================================================== #
def automate():
    print("Automating...")
    # wait for me to alt-ab
    time.sleep(3)

    loop = True
    while loop:
        if keyboard.is_pressed("t"):
            atkSeq()

        if keyboard.is_pressed("escape"):
            print("Exited...")
            break





# ======================================================== Call Funcs ======================================================== #
#

# Full Automation
automate()





# ======== Attack Sequence ======== #
# 1. check if menu is on screen
# 2. click through menu
# 3. wait
# 4. back to step 1

# ======== Encounter Sequence ======== #
# 1. 

