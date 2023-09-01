# libraries
import time

# automation functions
from island_loot_automation.screenshot_island import screenshotIsland
from island_loot_automation.scan_loot import scan, getLoot, clearLoot
from island_loot_automation.click_loot import click
from island_loot_automation.rebake import rebake
from island_loot_automation.next_map import nextMap


def automateLoot():
    time.sleep(2)

    # set islands to cover
    islands = 5

    for i in range(islands):
        # ===== Handle Diamonds ===== #
        print("=== Collecting Diamonds ===")
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
        
        # clear arr
        clearLoot()


        # ===== Handle Money ===== #
        print("=== Collecting Money ===")
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
        
        # clear arr
        clearLoot()


        # ===== Handle Crystals ===== #
        print("=== Collecting Crystals ===")
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
        
        # clear arr
        clearLoot()


        # ===== Handle Food ===== #
        print("=== Collecting Food ===")
        screenshotIsland()
        # scan for food
        scan("food", "./imgRef/island/currentIsland.png", 0.7, False)
        foodArr = getLoot()
        # set state for rebaking
        shouldRebake = False
        if len(foodArr) != 0: shouldRebake = True
        # collect all food
        while len(foodArr) != 0:
            # click food
            click(foodArr)
            # clear arr
            clearLoot()
            # take new screenshot for remainging food and incase click moved view
            screenshotIsland()
            # scan for remaming food
            scan("food", "./imgRef/island/currentIsland.png", 0.7, False)
            foodArr = getLoot()
        
        # clear arr
        clearLoot()


        # ===== Rebake ===== #
        # only rebake if food was collected
        if shouldRebake:
            print("Rebaking")
            # find bakery
            scan("bakery", "./imgRef/island/currentIsland.png", 0.9, False)
            bakery = getLoot()
            # remove all but first found instance
            bakery = bakery[:1]
            # click bakery
            click(bakery)
            # rebake
            rebake()


        # ===== Next Island ===== #
        print("=== Changing Island ===")
        nextMap()
