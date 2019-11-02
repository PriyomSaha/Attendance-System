import pyautogui as pg
import time

time.sleep(2)
pg.FAILSAFE = True
# def save():
#     time.sleep(2)
#     pg.click()
#     time.sleep(2)
#     pg.moveTo(350,615,2)
#     pg.click()
#     time.sleep(2)
#     pg.moveTo(300,560,2)
#     pg.click()
#     time.sleep(2)
#     pg.moveTo(400,450,2)
#     pg.click()
#     time.sleep(2)

# =============================================================================
# save_to_playlist_position = (350,615)
# playlist_position(test) = (300,560)
#Position of cross = (400,450)
# Window width is (600 x 1025) ie 2 video in one line
# =============================================================================
scroll=0
pg.moveTo(428,361,2)
while scroll == 0:
# =============================================================================
#     First video menu click
# =============================================================================
    
    time.sleep(10)
    pg.moveRel(0,288,2)
    
# =============================================================================
#     Second video menu click
# =============================================================================
    
    pg.moveRel(0,288,2)
    
# =============================================================================
#     Scroll and move to position
# =============================================================================
    
    pg.scroll(-150)
    scroll+=1
    print(pg.position())
