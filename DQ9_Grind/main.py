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





# ======================================================== Take Screenshot Func ======================================================== #
def captureScreenshot(fileName, mode, x, y, w, h):
    # take a screenshot of the screen and store it in memory, then
    # convert the PIL/Pillow image to an OpenCV compatible NumPy array
    # and finally write the image to disk
    if mode == "full":
        image = pygui.screenshot()
        image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
        cv.imwrite("./imgRef/" + fileName, image)
    elif mode == "coords":
        image = pygui.screenshot(region = (x, y, w, h))
        image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
        cv.imwrite("./imgRef/" + fileName, image)





# ======================================================== Get Current State Func ======================================================== #
def getGameStatus(imgPath1, imgPath2):
    # define imgs as variables 
    img1 = cv.imread("./imgRef/" + imgPath1 + ".png", cv.IMREAD_UNCHANGED)
    img2 = cv.imread("./imgRef/" + imgPath2 + ".png", cv.IMREAD_UNCHANGED)

    # check dimensions
    # print(
    #     img1.shape[0],
    #     img1.shape[1],
    #     img2.shape[0],
    #     img2.shape[1],
    # )

    # set a threshold for matching accuracy
    threshold = 0.9

    # match img2 against img1 with 1 of the following methods
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(img1, img2, method)
    
    # Get all positions from the match result that exceed the threshold (retunrs array)
    locations = np.where(result >= threshold)
    # refine the locations array to just return x and y coordinates of each matched location
    locations = list(zip(*locations[::-1]))

    # return true or false depending on if images matched
    if len(locations) >= 1:
        # print("p")
        return True
    else:
        # print("n")
        return False





# ======================================================== Attack Sequence Func ======================================================== #
def atkSeq():
    for i in range(10):
        pressKey("x")
        time.sleep(0.1)





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




# ======== Attack Sequence ======== #
# 1. check if menu is on screen
# 2. click through menu
# 3. wait
# 4. back to step 1

# ======== Encounter Sequence ======== #
# 1. 

