import pyautogui as pg
import time
time.sleep(5)
print(pg.position())
for i in range(120):
    time.sleep(5)
    pg.moveTo(1813,283)
    pg.click()
