# libraries
import time
import os

# automation functions
from automation.pair_operations import getAllPairs, locatePairs, getPairsArr
from automation.screenshot_operations import captureWindow
from automation.tile_operations import getUnknown, findTiles, getTilesArr, getTileImages


def automate():
    print("Automation Starting")
    # Give me 3 sec to change to right window
    time.sleep(3)
    # set length to 9 for 9 levels 
    length = 9
    # get tiles and pairs arr
    tiles = getTilesArr()
    pairs = getPairsArr()

    for i in range(length):
        print("\n\n========== New Iteration ==========")

        # ===== Set up ===== #
        # get current window view and set path
        windowPath = captureWindow()
        # find instance of unknown
        unknownNumber = getUnknown(windowPath, 0.7)
        # set unknown path
        unknownPath = "./imgRef/unknowns/unknown" + unknownNumber + ".png"
        print("Unknown Path:\t" + unknownPath)

        # ===== Run Main Funcs ===== #
        # find all unknown tiles
        findTiles(windowPath, unknownPath, thresholdVal = 0.7, mode = "rectangles", lineColor = (0, 255, 0))
        print("Current total tiles: " + str(len(tiles)))

        # get all revealed tile images
        getTileImages()

        # get all pairs
        getAllPairs()

        # find and locate all pairs
        locatePairs()
        # ========================== #

        # wait for level complete animation
        time.sleep(5)

        # delete all tile images
        print("\n\n==== Deleting all Tile Images ====\n")
        for i in range(len(tiles)):
            "./imgRef/tiles/img_" + str(i + 1) + ".png"
            os.remove("./imgRef/tiles/img_" + str(i + 1) + ".png")
        print("Tiles deleted successfully")
        # delete the screenshot
        os.remove("./imgRef/misc/currentBoard.png")
        print("Screenshot deleted")

        # remove everything in tiles and pairs arr to reset them to be used in next iteration
        print("\n\n==== Clearing arrays ====\n")
        tiles.clear()
        pairs.clear()
        print("Arrays cleared successfully")

        # wait 2s to be safe
        time.sleep(2)