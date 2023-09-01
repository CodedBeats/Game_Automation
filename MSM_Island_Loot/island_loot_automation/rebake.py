# libraries
import pyautogui
import time

def rebake():
    # wait for UI to open
    time.sleep(1)
    # click rebake
    pyautogui.moveTo(1060, 950)
    pyautogui.click()
    # wait for UI to switch
    time.sleep(0.5)
    # click confirm
    pyautogui.moveTo(680, 750)
    pyautogui.click()
    # wait for UI to close
    time.sleep(2)

    # center screen
    pyautogui.dragTo(700, 870, button="left")
    # wait just for my sake lol
    time.sleep(1)