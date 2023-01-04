import cv2 as cv
import numpy as np

# define imgs as variables 
pvz = cv.imread('./imgRef/PvZ.png', cv.IMREAD_UNCHANGED)
peaShooter = cv.imread('./imgRef/peaShooter.png', cv.IMREAD_UNCHANGED)

# get dimenshions of Pea Shooter img
peaShooterW = peaShooter.shape[1]
peaShooterH = peaShooter.shape[0]

# match shovel img against pvz img to see if it can be found
result = cv.matchTemplate(pvz, peaShooter, cv.TM_CCOEFF_NORMED)

# set a threshold for accuracy
threshold = 0.7
# get all coord possitions where it matches with this threshold
locations = np.where(result >= threshold)
# refine the locations array to just return x and y coordinates of each matched location
locations = list(zip(*locations[::-1]))

# create list of rectangles [x, y, w, h] (so they can be reduced) 
rectangles = []
for l in locations:
    rect = [int(l[0]), int(l[1]), peaShooterW, peaShooterH]
    # add rectangle to rectangles arr twice (since if there is only 1 rect at a poss it will eliminate it when grouping)
    rectangles.append(rect)
    rectangles.append(rect)

# group rectangles that are close to each other where 3rd parameter controls how close together they must be to be grouped
rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)


if len(rectangles):
    print("Found some Pea Shooters")

    # set rect properties
    lineColor = (0, 0, 255) # (B,G,R)
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
        # draw the box
        cv.rectangle(pvz, topLeft, bottomRight, lineColor, lineThickness, lineType)

    # draw rectangle where the is match is located
    cv.imshow("Matched Image", pvz)
    cv.waitKey()

else:
    print("Didn't find any pea shooters")
