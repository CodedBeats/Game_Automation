# libraries
import cv2 as cv
import numpy as np
import pyautogui


# take screenshots at found instances
def screenshotIsland():
    # take a screenshot of the screen and store it in memory, then
    image = pyautogui.screenshot()
    # convert the PIL/Pillow image to an OpenCV compatible NumPy array
    image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    # write the image to disk
    cv.imwrite("./imgRef/island/currentIsland.png", image)