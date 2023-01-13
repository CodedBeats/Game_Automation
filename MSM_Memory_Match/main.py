import cv2 as cv
import numpy as np
import pyautogui
import time
import os
import re

# ======================================================== Classes ======================================================== #
# declare tile class to create instances and add to arr of tiles
class tile:
    def __init__(self, tileName, x, y, w, h, centerX, centerY):
        self.tileName = tileName
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.centerX = centerX
        self.centerY = centerY
tiles = []

# declare pair class for matching pairs
class pair:
    def __init__(self, pairName, t1, t2):
        self.pairName = pairName
        self.t1 = t1
        self.t2 = t2
pairs = []





# ======================================================== Find Tile Coords Func ======================================================== #
def findTiles(baseImagePath, isolatedImagePath, thresholdVal, mode, lineColor = (0, 0, 255)):
    # set tiles arr to empty here since we want it to reset every time this func is called in automate()
    # tiles = []

    # define imgs as variables 
    baseImage = cv.imread(baseImagePath, cv.IMREAD_UNCHANGED)
    isolatedImage = cv.imread(isolatedImagePath, cv.IMREAD_UNCHANGED)
    # save dimenshions of Pea Shooter img
    isolatedImageW = isolatedImage.shape[1]
    isolatedImageH = isolatedImage.shape[0]

    # set a threshold for matching accuracy
    threshold = thresholdVal

    # match isolatedImage against baseImage with 1 of the following methods
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(baseImage, isolatedImage, method)
    
    # Get all positions from the match result that exceed the threshold (retunrs array)
    locations = np.where(result >= threshold)
    # refine the locations array to just return x and y coordinates of each matched location
    locations = list(zip(*locations[::-1]))

    # create list of rectangles [x, y, w, h] (so they can be grouped together) 
    rectangles = []
    for l in locations:
        rect = [int(l[0]), int(l[1]), isolatedImageW, isolatedImageH]
        # Add every box to the list twice in order to retain single (non-overlapping) boxes
        rectangles.append(rect)
        rectangles.append(rect)

    # group rectangles that are close to each other where 3rd parameter controls how close together they must be to be grouped
    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)

    points = []
    if len(rectangles):
        # set counter to 1 for naming convention
        counter = 1
        # set rect properties
        lineColor = lineColor # (B,G,R)
        lineThickness = 2
        lineType = cv.LINE_8
        markerColor = lineColor # (B,G,R)
        markerType = cv.MARKER_CROSS
        markerSize = 30
        markerThickness = 2

        # loop over each location
        for (x, y, w, h) in rectangles:
            # determine rect pos
            topLeft = (x, y)
            bottomRight = (x + w, y + h)
            # get center of rect
            centerX = x + int(w/2)
            centerY = y + int(h/2)
            # add rect data to tiles arr
            tiles.append(tile("tile_" + str(counter), x, y, w, h, centerX, centerY))

            if mode == "rectangles":
                # draw the rect
                cv.rectangle(baseImage, topLeft, bottomRight, lineColor, lineThickness, lineType)

            elif mode == "points":
                # save points
                points.append((centerX, centerY))
                # draw the center point
                cv.drawMarker(baseImage, (centerX, centerY), markerColor, markerType, markerSize, markerThickness)
            # increment counter
            counter += 1

        if mode:
            # display baseImage with matched data
            # cv.imshow("Matched Image", baseImage)
            # cv.waitKey()
            print("didn't show rects")
            # save the image
            # cv.imwrite('result_click_point.jpg', haystack_img)


    else:
        print("Didn't find any matches")





# ======================================================== Take Screenshot Func ======================================================== #
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






# ======================================================== Get Tile Images Func ======================================================== #
def getTileImages():
    # new section of data display
    print("\n\n==== Tile Image Data ====\n")
    # wait for me to switch windows
    time.sleep(4)

    counter = 1
    length = len(tiles)
    # iterate over each tile in tiles arr
    for i in range(length):
        print(
            "tile name: " + tiles[i].tileName,
            "\n\tx coord: " + str(tiles[i].x), 
            "\n\ty coord: " + str(tiles[i].y), 
            "\n\twidth val: " + str(tiles[i].w), 
            "\n\theight val: " + str(tiles[i].h), 
            "\n\tcenter x coord: " + str(tiles[i].centerX), 
            "\n\tcenter y coord: " + str(tiles[i].centerY),
            "\n----\n"
        )
        # move cursor to tile
        pyautogui.moveTo(tiles[i].centerX, tiles[i].centerY + 20)
        # click tile to reveal image
        pyautogui.click()
        time.sleep(0.5)
        # take image at given coords
        captureScreenshot("./tiles/img_" + str(counter) + ".png", "coords", tiles[i].x, tiles[i].y, tiles[i].w, tiles[i].h)
        # # temp y coord for game cloe
        # captureScreenshot("./tiles/img_" + str(counter) + ".png", "coords", tiles[i].x, tiles[i].centerY, tiles[i].w, tiles[i].h)
        counter += 1
        time.sleep(0.5)





# ======================================================== Match Pair Func ======================================================== #
def matchPair(imgPath1, imgPath2, thresholdVal):
    # define imgs as variables 
    img1 = cv.imread(imgPath1, cv.IMREAD_UNCHANGED)
    img2 = cv.imread(imgPath2, cv.IMREAD_UNCHANGED)

    # check dimensions
    # print(
    #     img1.shape[0],
    #     img1.shape[1],
    #     img2.shape[0],
    #     img2.shape[1],
    # )

    # set a threshold for matching accuracy
    threshold = thresholdVal

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





# ======================================================== Get All Pairs Func ======================================================== #
def getAllPairs(mode):
    # set pairs arr to empty here since we want it to reset every time this func is called in automate()
    # pairs = []
    # new section of data display
    print("\n\n==== Tile Matches ====\n")
    
    if mode == "tiles":
        pairCount = 0
        # get length for both loops
        length = len(tiles)
        # have exclude list so we don't get 2x pairs (2 and 4 match, 4 and 2 match)
        matched = []

        # loop through all tiles to match all against all (brute force I guess)
        for i in range(length):
            # print(matched)

            for j in range(length):
                # if i already has it's match, we skip to next i
                if i in matched:
                    break
                # if we are comparing the same image, we skip to next j
                elif i == j:
                    j += 1
                    continue

                else:
                    # compare image i and j
                    checkMatch = matchPair("./imgRef/tiles/img_" + str(i + 1) + ".png", "./imgRef/tiles/img_" + str(j + 1) + ".png", thresholdVal = 0.8)
                    # if they match we increment pairCount and add i to the matched arr
                    if checkMatch:
                        pairCount += 1
                        matched.append(i)
                        matched.append(j)
                        print("Pair " + str(pairCount) + ": ", str(i + 1) + " and " + str(j + 1))

                        # added a new pair and give thir x and y coords as centerX and centerY of tiles i and j respectively
                        pairs.append(pair("Pair_" + str(pairCount), [tiles[i].centerX, tiles[i].centerY], [tiles[j].centerX, tiles[j].centerY]))

                    # print("\npairs: " + str(pairCount), "\nimg: " + str(i + 1), "\nimg: " + str(j + 1), "\nmatched: " + str(doesMatch))
    
    elif mode == "boards":
        # set length to the amount of boards
        length = 10
        # take screenshot of whole window (the 0s are just there to fill params, they don't do anything)
        captureScreenshot("./misc/currentBoard.png", "full", 0, 0, 0, 0)
        print("Screenshot taken")

        # loop through all board images
        for i in range(length):
            # check if currentBoard is the same as board i
            checkMatch = matchPair("./imgRef/misc/currentBoard.png", "./imgRef/boards/board" + str(i + 1) + ".png", thresholdVal = 0.9)
            # if it matches, return that board file path
            if checkMatch:
                # set match as the board path
                currentBoardPath = "./imgRef/boards/board" + str(i + 1) + ".png"
                print("Matched with board" + str(i + 1))
                return currentBoardPath
            else:
                print("Couldn't Match a Board")

        # delete the screenshot
        # os.remove("./imgRef/misc/currentBoard.png")
        # print("Screenshot deleted")






# ======================================================== Find and Locate All Pairs Func ======================================================== #
def locatePairs():
    # new section of data display
    print("\n\n==== Pair Positions ====\n")
    length = len(pairs)
    for i in range(length):
        time.sleep(0.2)
        print(
            pairs[i].pairName,
            "\nPosition 1 - \n\t" + "x: " + str(pairs[i].t1[0]) + "\n\ty: " + str(pairs[i].t1[1]), 
            "\nPosition 2 - \n\t" + "x: " + str(pairs[i].t2[0]) + "\n\ty: " + str(pairs[i].t2[1]),
            "\n-------------"
        )

        # move to tile1 of pair and click
        pyautogui.moveTo(pairs[i].t1[0], pairs[i].t1[1])
        # game clone coords
        # pyautogui.moveTo(pairs[i].t1[0], pairs[i].t1[1] + 20)
        pyautogui.click()
        time.sleep(0.2)
        # move to tile2 of pair and click
        pyautogui.moveTo(pairs[i].t2[0], pairs[i].t2[1])
        # game clone coords
        # pyautogui.moveTo(pairs[i].t2[0], pairs[i].t2[1] + 20)
        pyautogui.click()
        time.sleep(0.2)
        




# ======================================================== Startup Function ======================================================== #
def automate():
    print("Automation Starting")
    # Give me 5 sec to change to right window
    time.sleep(5)
    # set length to 9 for 9 levels 
    length = 9

    for i in range(length):

        # get board path
        boardPath = getAllPairs("boards")
        # get all numbers in boardPath
        unknownNumberList = re.findall("\d+", boardPath)
        # use that number to set unknown path
        unknownPath = "./imgRef/unknowns/unknown" + str(unknownNumberList[0]) + ".png"
        print("Board Path: " + boardPath, "\n Unknown Path: " + unknownPath)

        # ===== Run Main Funcs ===== #
        # find all unknown tiles
        findTiles(boardPath, unknownPath, thresholdVal = 0.8, mode = "rectangles", lineColor = (0, 255, 0))
        print(len(tiles))

        # get all revealed tile images
        getTileImages()

        # get all pairs
        getAllPairs("tiles")

        # find and locate all pairs
        locatePairs()
        # ========================== #

        # wait for level complete animation
        # time.sleep(3)
        # delete all tile images
        # for i in range(len(tiles)):
        #     "./imgRef/tiles/img_" + str(i + 1) + ".png"
        #     os.remove("./imgRef/tiles/img_" + str(i + 1) + ".png")

        # wait 2s to be safe
        time.sleep(3)


# 1. reset tiles and pairs arr on each iteration of loop
# 2. delete tile imgaes after each iteration of loop




# ======================================================== Call Funcs ======================================================== #
# # find all tiles
# findTiles("./imgRef/boards/board9.png", "./imgRef/unknowns/unknown9.png", thresholdVal = 0.8, mode = "rectangles", lineColor = (0, 255, 0))

# # get all revealed tile images
# getTileImages()

# # get all pairs
# getAllPairs("tiles")

# # find and locate all pairs
# locatePairs()

# Whoop Whoop
automate()
