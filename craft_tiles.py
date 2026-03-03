import subprocess
from time import sleep


def default_sleep():
    # sleep before every tap, swipe or other operation
    sleep(0.1)

def adb(command):
    subprocess.run(["adb"] + command.split())

def tap(x, y):
    adb(f"shell input tap {x} {y}")
    default_sleep()

def swipe(x1, y1, x2, y2, duration=500):
    adb(f"shell input swipe {x1} {y1} {x2} {y2} {duration}")
    default_sleep()

def select_and_buy():
    # click the buy button
    tap(1666, 888)
    
    # select max amount
    swipe(1400, 775, 1668, 775, 100)

    # click the tick sign/buy
    tap(1440, 910)

    # error handling incase of no tile available
    tap(1670, 500)
    
def lower_tile_operation():
    x=1145
    y=360
    # selecting tiles from lower second row
    for i in range(4):
        tap(x,y)
        select_and_buy()
        x-=130

    # selecting tiles from lower first row
    x=1400
    y=220
    for i in range(6):
        tap(x,y)
        select_and_buy()
        x-=125

def upper_tile_operation():
    x=1400
    y=800
    for i in range(5):
        for j in range(6):
            tap(x,y)
            select_and_buy()
            x-=125
        x=1400
        y-=140

def main():
    # ---- GAME AUTOMATION START ----
    print("Starting...")
    # time to open game manually
    # sleep(3) 

    # 1. Click bag icon
    tap(148, 307)

    # 2. Click tool/craft icon
    tap(1280, 916)

    # 3. Click on the star icon
    tap(623,859)

    # 4. perform operation with the lower tiles
    lower_tile_operation()

    # 5. Swipe down and go the tile begining section
    swipe(1000, 160, 1000, 329, 150)

    # 6. upper_tile_operation
    upper_tile_operation()
    # 7. all operation end
    print("Automation Finished")

if __name__=="__main__":
    # main()
    swipe(545, 53, 537, 1048, 800)