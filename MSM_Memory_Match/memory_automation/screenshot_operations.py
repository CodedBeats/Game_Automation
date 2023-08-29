import cv2 as cv
import numpy as np
import pyautogui


# take screenshots at found instances
def captureScreenshot(fileName, mode, x, y, w, h):
    # take a screenshot of the screen and store it in memory, then
    # convert the PIL/Pillow image to an OpenCV compatible NumPy array
    # and finally write the image to disk
    if mode == "full":
        image = pyautogui.screenshot()
        image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
        cv.imwrite("./imgRef/" + fileName, image)
    elif mode == "coords":
        image = pyautogui.screenshot(region = (x, y, w, h))
        image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
        cv.imwrite("./imgRef/" + fileName, image)



# take screenshot of entire window
def captureWindow():
    # take screenshot of whole window (the 0s are just there to fill params, they don't do anything)
    captureScreenshot("misc/currentBoard.png", "full", 0, 0, 0, 0)
    print("Screenshot taken")
    return "./imgRef/misc/currentBoard.png"