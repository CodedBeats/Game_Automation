# libraries
import cv2 as cv
import numpy as np

# declare loot class to create instances and add to an arr
class Loot:
    def __init__(self, lootName, x, y, w, h, centerX, centerY):
        self.lootName = lootName
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.centerX = centerX
        self.centerY = centerY
loot = []


# scan for loot type
def scan(lootType, baseImagePath, threshold, isTesting, lineColor = (0, 0, 255)):

    # define island img as variable
    islandImage = cv.imread(baseImagePath, cv.IMREAD_UNCHANGED)

    # set loot img path
    lootImgPath = ""
    if (lootType == "diamond"):
        lootImgPath = "./imgRef/islandLoot/diamond.png"
    elif (lootType == "food"):
        lootImgPath = "./imgRef/islandLoot/food.png"
    elif (lootType == "money"):
        lootImgPath = "./imgRef/islandLoot/money.png"
    elif (lootType == "crystal"):
        lootImgPath = "./imgRef/islandLoot/crystal.png"
    elif (lootType == "bakery"):
        lootImgPath = "./imgRef/islandLoot/bakery.png"
    # define loot img as variable 
    lootImg = cv.imread(lootImgPath, cv.IMREAD_UNCHANGED)

    # save dimenshions of loot
    lootImgW = lootImg.shape[1]
    lootImgH = lootImg.shape[0]

    # match lootImg against islandImage with 1 of the following methods
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(islandImage, lootImg, method)
    
    # Get all positions from the match result that exceed the threshold (retunrs array)
    locations = np.where(result >= threshold)
    # refine the locations array to just return x and y coordinates of each matched location
    locations = list(zip(*locations[::-1]))

    # create list of rectangles [x, y, w, h] (so they can be grouped together) 
    rectangles = []
    for l in locations:
        rect = [int(l[0]), int(l[1]), lootImgW, lootImgH]
        # Add every box to the list twice in order to retain single (non-overlapping) boxes
        rectangles.append(rect)
        rectangles.append(rect)

    # group rectangles that are close to each other where 3rd parameter controls how close together they must be to be grouped
    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)

    if len(rectangles):
        # set counter to 1 for naming convention
        counter = 1
        # set rect properties
        lineColor = lineColor # (B,G,R)
        lineThickness = 2
        lineType = cv.LINE_8

        # loop over each location
        for (x, y, w, h) in rectangles:
            # determine rect pos
            topLeft = (x, y)
            bottomRight = (x + w, y + h)
            # get center of rect
            centerX = x + int(w/2)
            centerY = y + int(h/2)
            # add rect data to tiles arr
            loot.append(Loot(lootType + "_" + str(counter), x, y, w, h, centerX, centerY))
            # draw the rect
            cv.rectangle(islandImage, topLeft, bottomRight, lineColor, lineThickness, lineType)

            # increment counter
            counter += 1

        if isTesting:
            # display islandImage with matched data
            cv.imshow("Matched Image", islandImage)
            cv.waitKey()
            print("all " + lootType + " loot found")

    else:
        print("No " + lootType + " loot found")


# get loot arr
def getLoot():
    return loot

# clear arr
def clearLoot():
    loot.clear()
