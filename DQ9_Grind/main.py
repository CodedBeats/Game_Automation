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
# Full Automation
automate()



# ======== OverHaul ======== #
# ===Sequence===
#   WHILE loop
#       get img
#       IF img == blackScreen
#           wait ?s
#       END IF
#       gameStatus = match(img)
#       IF gameStatus == combat        
#           stratergy = 0 - 10
#           IF stratergy > 3
#               battleSequence(x, right, x, rainOfPain, x, x, down, down, x, x)
#           ELSE
#               battleSequence(x, right, x, hallowedArrow, x, x, down, down, x, x)
#           END IF
#       ELSE IF gameStatus == exploration
#           explore()
#       END IF
#   END WHILE