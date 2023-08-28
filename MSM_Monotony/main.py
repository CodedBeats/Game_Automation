import pyautogui as py
import time


# === Breeding Automation === #

def breeed():
    # breeding structure
    print("breeding structure")
    py.click(530, 360)
    time.sleep(2)

    # breed button
    print("breed button")
    py.click(1370, 960)
    time.sleep(2)

    # retry button
    print("retry button")
    py.click(1530, 960)
    time.sleep(2)

    # confirm breed
    print("confirm breed")
    py.click(760, 870)
    # edit to breed time + 3
    time.sleep(50)

    # breeded monster
    print("breeded monster")
    py.click(530, 320)
    time.sleep(2)

    # zap button
    print("zap button")
    py.click(950, 710)
    time.sleep(2)

    # zap to celestial/wublin
    print("zap to celestial/wublin")
    py.click(640, 670)
    time.sleep(2)

    # confirm zap
    print("confirm zap\n")
    py.click(680, 760)
    time.sleep(2)





def automate():
    loop = True
    iterationCount = 0

    # alt tab time
    time.sleep(3)
    # print(py.position())
    while loop:
        print(iterationCount)
        breeed()
        iterationCount += 1



automate()
