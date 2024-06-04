# libraries
import time
import os
import random
import pygetwindow

# automation functions
from memory_automation.pair_operations import sortPairs, locatePairs, getPairsArr
from memory_automation.screenshot_operations import captureWindow
from memory_automation.tile_operations import getUnknownTileSize, findTileInstances, getTilesArr, getTileImages


def automateMemoryMatch():
    print("Automation Starting")
    # switch to my singing monsters app
    msmwindow = pygetwindow.getWindowsWithTitle('My Singing Monsters')[0]
    msmwindow.activate()
    time.sleep(1)
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
        unknownNumber = getUnknownTileSize(windowPath, 0.7)
        # set unknown path
        unknownPath = "./imgRef/unknowns/unknown" + unknownNumber + ".png"
        print("Unknown Path:\t" + unknownPath)

        # ===== Run Main Funcs ===== #
        # find all unknown tiles
        findTileInstances(windowPath, unknownPath, thresholdVal = 0.7, mode = "rectangles", lineColor = (0, 255, 0))
        print("Current total tiles: " + str(len(tiles)))

        # get all revealed tile images
        getTileImages()

        # get all pairs
        sortPairs()

        # find and locate all pairs
        locatePairs()
        # ========================== #
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

        # wait for level complete animation
        time.sleep(3)


