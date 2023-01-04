import cv2 as cv
import numpy as np

# define imgs as variables 
pvz = cv.imread('./imgRef/PvZ.png', cv.IMREAD_UNCHANGED)
pvzShovel = cv.imread('./imgRef/PvZ_Shovel.png', cv.IMREAD_UNCHANGED)

# match shovel img against pvz img to see if it can be found
result = cv.matchTemplate(pvz, pvzShovel, cv.TM_CCOEFF_NORMED)


# display brightness map image (where the brightest pixels are what match the shovel img)
# == cv.imshow("Results", result)
# need to pause otherwise it insta exits
# == cv.waitKey()


# get best match possition where maxVal is confidence in the img matching (1 is 100%)
minVal, maxVal, milLoc, maxLoc = cv.minMaxLoc(result)

# set threshold for the match
threshold = 0.8
if maxVal >= threshold:
    print("Found the shovel with: %s" % str(maxVal), "accuracy")

    # get dimenshions of shovel img
    shovelW = pvzShovel.shape[1]
    shovelH = pvzShovel.shape[0]

    topLeft = maxLoc
    bottomRight = (topLeft[0] + shovelW, topLeft[1] + shovelH)

    # draw rectangle where the is match is located
    cv.rectangle(pvz, topLeft, bottomRight, color = (0, 255, 0), thickness = 2, lineType = cv.LINE_8)
    cv.imshow("Matched Image", pvz)
    cv.waitKey()

else:
    print("Didn't find the shovel")
