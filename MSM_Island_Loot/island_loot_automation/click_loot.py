# libraries
import pyautogui
import time

# click each found instance of loot
def click(lootArr):
    for i in range(len(lootArr)):
        # move to loot and click
        pyautogui.moveTo(lootArr[i].centerX, lootArr[i].centerY)
        pyautogui.click()
        time.sleep(0.2)
