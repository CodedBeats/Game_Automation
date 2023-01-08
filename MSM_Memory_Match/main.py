import cv2 as cv
import numpy as np
import pyautogui
import time
import imutils

# ======================================================== Tile Class ======================================================== #
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

# ======================================================== Pairs Class ======================================================== #
# declare pair class for matching pairs
class pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y





# ======================================================== Find Tile Coords Func ======================================================== #
def findImageMatches(baseImagePath, isolatedImagePath, thresholdVal, mode, lineColor = (0, 0, 255)):

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
    
    # Get all positions from the match result that exceed the threshold
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
            cv.imshow("Matched Image", baseImage)
            cv.waitKey()
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
    elif mode == "coords":
        image = pyautogui.screenshot(region = (x, y, w, h))

    image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    cv.imwrite("./imgRef/" + fileName, image)





# ======================================================== Get Tile Images Func ======================================================== #
def getTileImages():
    # wait for me to switch windows
    time.sleep(4)

    counter = 1
    length = len(tiles)
    # iterate of each tile in tiles arr
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
        counter += 1
        time.sleep(1)





# ======================================================== Call Funcs ======================================================== #
# find all matches
findImageMatches("./imgRef/boards/boardClone.png", "./imgRef/unknowns/unknownTileClone.png", thresholdVal = 0.75, mode = "rectangles", lineColor = (0, 255, 0))
# create images for each match found
getTileImages()