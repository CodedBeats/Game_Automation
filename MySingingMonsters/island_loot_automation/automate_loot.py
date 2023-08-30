# libraries
import time

# automation functions
from island_loot_automation.screenshot_island import screenshotIsland
from island_loot_automation.scan_loot import scan, getLoot, clearLoot
from island_loot_automation.click_loot import click


def automateLoot():
    time.sleep(2)

    # set islands to cover
    islands = 1

    for i in range(islands):
        # ===== Handle Diamonds ===== #
        print("Collecting Diamonds")
        screenshotIsland()
        # scan for diamonds
        scan("diamond", "./imgRef/island/currentIsland.png", 0.7, False)
        diamondArr = getLoot()
        # collect all diamonds
        while len(diamondArr) != 0:
            # click diamond
            click(diamondArr)
            # clear arr
            clearLoot()
            # take new screenshot for remainging diamonds and incase click moved view
            screenshotIsland()
            # scan for remaming diamonds
            scan("diamond", "./imgRef/island/currentIsland.png", 0.7, False)
            diamondArr = getLoot()


        # ===== Handle Food ===== #
        print("Collecting Food")
        screenshotIsland()
        # scan for food
        scan("food", "./imgRef/island/currentIsland.png", 0.7, False)
        fooddArr = getLoot()
        # set state for rebaking
        shouldRebake = False
        if len(fooddArr) != 0: shouldRebake = True
        # collect all food
        while len(fooddArr) != 0:
            # click food
            click(fooddArr)
            # clear arr
            clearLoot()
            # take new screenshot for remainging food and incase click moved view
            screenshotIsland()
            # scan for remaming food
            scan("food", "./imgRef/island/currentIsland.png", 0.7, False)
            fooddArr = getLoot()


        # ===== Rebake ===== #
        # only rebake if food was collected
        if shouldRebake:
            print("Rebaking")
            # click bakery
            # click rebake
            # click confirm


        # ===== Handle Money ===== #
        print("Collecting Money")
        screenshotIsland()
        # scan for money
        scan("money", "./imgRef/island/currentIsland.png", 0.7, False)
        moneyArr = getLoot()
        # collect all money
        while len(moneyArr) != 0:
            # click money
            click(moneyArr)
            # clear arr
            clearLoot()
            # take new screenshot for remainging money and incase click moved view
            screenshotIsland()
            # scan for remaming money
            scan("money", "./imgRef/island/currentIsland.png", 0.7, False)
            moneyArr = getLoot()


        # ===== Handle Crystals ===== #
        print("Collecting Crystals")
        screenshotIsland()
        # scan for crystals
        scan("crystal", "./imgRef/island/currentIsland.png", 0.7, False)
        crystalArr = getLoot()
        # collect all crystals
        while len(crystalArr) != 0:
            # click crystal
            click(crystalArr)
            # clear arr
            clearLoot()
            # take new screenshot for remainging crystals and incase click moved view
            screenshotIsland()
            # scan for remaming crystals
            scan("crystal", "./imgRef/island/currentIsland.png", 0.7, False)
            crystalArr = getLoot()


        # ===== Next Island ===== #
        print("Changing Island")
        # click map
        # click right arrow
        # click go
