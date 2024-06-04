# libraries
import pyautogui
import time

def nextMap():
    # click map
    pyautogui.moveTo(1060, 950)
    pyautogui.click()
    # wait for UI to open
    time.sleep(1)
    # click next
    pyautogui.moveTo(1840, 570)
    pyautogui.click()
    # wait for island to switch
    time.sleep(1)
    # click go
    pyautogui.moveTo(960, 980)
    pyautogui.click()
    # wait for next island to load
    time.sleep(8.5)