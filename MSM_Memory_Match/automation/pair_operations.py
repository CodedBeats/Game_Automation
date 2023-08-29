# libraries
import cv2 as cv
import numpy as np
import pyautogui
import time

# automation functions
from automation.tile_operations import getTilesArr


# declare pair class for matching pairs
class Pair:
    def __init__(self, pairName, t1, t2):
        self.pairName = pairName
        self.t1 = t1
        self.t2 = t2
pairs = []



# get pairs arr
def getPairsArr():
    return pairs


# check if 2 imgs match
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
    


# sort into pairs
def getAllPairs():
    # get tiles arr
    tiles = getTilesArr()

    # new section of data display
    print("\n\n==== Getting All Tile Pairs ====\n")
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
                    pairs.append(Pair("Pair_" + str(pairCount), [tiles[i].centerX, tiles[i].centerY], [tiles[j].centerX, tiles[j].centerY]))

                # print("\npairs: " + str(pairCount), "\nimg: " + str(i + 1), "\nimg: " + str(j + 1), "\nmatched: " + str(doesMatch))



# reveal all pairs (completing board)
def locatePairs():
    # new section of data display
    print("\n\n==== Locating All Pairs ====\n")
    length = len(pairs)
    for i in range(length):
        time.sleep(0.2)
        # print(
        #     pairs[i].pairName,
        #     "\nPosition 1 - \n\t" + "x: " + str(pairs[i].t1[0]) + "\n\ty: " + str(pairs[i].t1[1]), 
        #     "\nPosition 2 - \n\t" + "x: " + str(pairs[i].t2[0]) + "\n\ty: " + str(pairs[i].t2[1]),
        #     "\n-------------"
        # )

        # move to tile1 of pair and click
        pyautogui.moveTo(pairs[i].t1[0], pairs[i].t1[1])
        pyautogui.click()
        time.sleep(0.2)
        # move to tile2 of pair and click
        pyautogui.moveTo(pairs[i].t2[0], pairs[i].t2[1])
        pyautogui.click()
        time.sleep(0.2)
    print("All pairs located successfully")