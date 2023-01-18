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


def pyClick(x, y):
    pygui.click(x,y)
    pygui.mouseDown()
    pygui.mouseUp()





# ======================================================== Startup Func ======================================================== #
def automate():
    print("Automating...")
    # wait for me to alt-ab
    time.sleep(3)

    loop = True
    battle = True

    while loop:
        while battle:
            pressKey("x")
            time.sleep(0.5)
            if keyboard.is_pressed("e"):
                battle = False


        if keyboard.is_pressed("r"):
            battle = True


        if keyboard.is_pressed("escape"):
            print("Exited...")
            break





# ======================================================== Call Funcs ======================================================== #
#

# Full Automation
automate()
